const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

class Element {
  constructor() { this.value = ""; this.textContent = ""; this.dataset = {}; this.listeners = {}; this.children = []; }
  addEventListener(name, handler) { this.listeners[name] = handler; }
  setAttribute(name, value) { this[name] = value; }
  append(...items) { this.children.push(...items); }
  replaceChildren() { this.children = []; }
}

function setup() {
  const elements = Object.fromEntries(["contactForm", "contacts", "status", "reload"].map(id => [id, new Element()]));
  const form = elements.contactForm;
  const submit = new Element();
  form.querySelector = () => submit;
  form.elements = Object.fromEntries(["name", "age", "gender", "phoneNumber", "email"].map(name => [name, new Element()]));
  Object.assign(form.elements.name, { value: "Alice" });
  Object.assign(form.elements.age, { value: "30" });
  Object.assign(form.elements.gender, { value: "0" });
  Object.assign(form.elements.phoneNumber, { value: "+49 0123" });
  Object.assign(form.elements.email, { value: "alice@example.com" });
  form.resetCalls = 0;
  form.reset = () => { form.resetCalls++; };
  const requests = [];
  const responses = [];
  const context = vm.createContext({
    document: { getElementById: id => elements[id], createElement: () => new Element() },
    fetch: async (url, options) => {
      requests.push({ url, options });
      const next = responses.shift();
      if (next instanceof Error) throw next;
      return next || { ok: true, status: 200, json: async () => [] };
    }
  });
  vm.runInContext(fs.readFileSync(path.join(__dirname, "../Beispiele/Adressbuch/Api/wwwroot/script.js"), "utf8"), context);
  const settle = async () => { for (let i = 0; i < 8; i++) await new Promise(resolve => setImmediate(resolve)); };
  return { elements, form, submit, requests, responses, settle, context };
}

test("POST sends all required fields and only successful saving clears the form", async () => {
  const app = setup(); await app.settle();
  app.responses.push({ ok: true, status: 201, json: async () => ({ id: 1 }) });
  app.form.listeners.submit({ preventDefault() {} }); await app.settle();
  const post = app.requests.find(item => item.options?.method === "POST");
  assert.deepEqual(JSON.parse(post.options.body), {
    name: "Alice", age: 30, gender: 0, phoneNumber: "+49 0123", email: "alice@example.com"
  });
  assert.equal(app.form.resetCalls, 1);
  assert.equal(app.elements.status.textContent, "Kontakt hinzugefügt.");
});

test("HTTP 400 keeps the form and shows validation errors", async () => {
  const app = setup(); await app.settle();
  app.responses.push({ ok: false, status: 400, json: async () => ({ errors: { Email: ["E-Mail ungültig."] } }) });
  app.form.listeners.submit({ preventDefault() {} }); await app.settle();
  assert.equal(app.form.resetCalls, 0);
  assert.match(app.elements.status.textContent, /E-Mail ungültig/);
  assert.equal(app.elements.status.dataset.error, "true");
  assert.equal(app.submit.disabled, false);
});

test("network errors remain visible and preserve inputs", async () => {
  const app = setup(); await app.settle();
  app.responses.push(new Error("Server nicht erreichbar"));
  app.form.listeners.submit({ preventDefault() {} }); await app.settle();
  assert.equal(app.form.resetCalls, 0);
  assert.match(app.elements.status.textContent, /Server nicht erreichbar/);
});

test("refresh failure after saving reports the successful save separately", async () => {
  const app = setup(); await app.settle();
  app.responses.push({ ok: true, status: 201, json: async () => ({ id: 1 }) }, new Error("Abruf fehlgeschlagen"));
  app.form.listeners.submit({ preventDefault() {} }); await app.settle();
  assert.equal(app.form.resetCalls, 1);
  assert.match(app.elements.status.textContent, /Kontakt hinzugefügt.*Liste konnte nicht aktualisiert/);
});

test("contacts render as text and DELETE accepts an empty 204 response", async () => {
  const app = setup(); await app.settle();
  app.responses.push({ ok: true, status: 200, json: async () => [{ id: 7, name: "<b>Alice</b>", phoneNumber: "123", email: "alice@example.com" }] });
  app.elements.reload.listeners.click(); await app.settle();
  const [text, remove] = app.elements.contacts.children[0].children;
  assert.match(text.textContent, /<b>Alice<\/b>/);
  app.responses.push({ ok: true, status: 204, json: async () => { throw new Error("204 must not be parsed"); } });
  remove.listeners.click(); await app.settle();
  assert.equal(app.requests.find(item => item.options?.method === "DELETE").url, "/api/contacts/7");
  assert.equal(app.elements.status.textContent, "Kontakt gelöscht.");
});
