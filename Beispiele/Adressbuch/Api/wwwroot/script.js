// Bei separatem Hosting auf http://localhost:5500 die API ausdrücklich angeben:
// const apiUrl = "http://localhost:5000/api/contacts";
const apiUrl = "/api/contacts";
const form = document.getElementById("contactForm");
const list = document.getElementById("contacts");
const status = document.getElementById("status");
const submit = form.querySelector("button[type=submit]");
const reload = document.getElementById("reload");
let busy = false;

function message(text, isError = false) {
  status.textContent = text;
  status.dataset.error = String(isError);
}

async function request(url, options) {
  const response = await fetch(url, options);
  if (!response.ok) {
    let detail = `HTTP ${response.status}`;
    try {
      const problem = await response.json();
      detail = problem.errors ? Object.values(problem.errors).flat().join(" ") : problem.title || detail;
    } catch { /* Antworten ohne JSON behalten den HTTP-Status. */ }
    throw new Error(detail);
  }
  return response.status === 204 ? null : response.json();
}

async function fetchContacts() {
  const contacts = await request(apiUrl);
  list.replaceChildren();
  for (const contact of contacts) {
    const li = document.createElement("li");
    const text = document.createElement("span");
    text.textContent = `${contact.name} — ${contact.phoneNumber} — ${contact.email}`;
    const remove = document.createElement("button");
    remove.type = "button";
    remove.textContent = "Löschen";
    remove.setAttribute("aria-label", `${contact.name} löschen`);
    remove.addEventListener("click", () => runAction(async () => {
      await request(`${apiUrl}/${contact.id}`, { method: "DELETE" });
      await refreshAfterMutation("Kontakt gelöscht.");
    }));
    li.append(text, remove);
    list.append(li);
  }
}

async function refreshAfterMutation(success) {
  try {
    await fetchContacts();
    message(success);
  } catch (error) {
    message(`${success} Die Liste konnte nicht aktualisiert werden: ${error.message}`, true);
  }
}

async function runAction(action) {
  if (busy) return;
  busy = true;
  submit.disabled = reload.disabled = true;
  message("Bitte warten …");
  try { await action(); }
  catch (error) { message(`Fehler: ${error.message}`, true); }
  finally { busy = false; submit.disabled = reload.disabled = false; }
}

form.addEventListener("submit", event => {
  event.preventDefault();
  const input = {
    name: form.elements.name.value.trim(),
    age: Number(form.elements.age.value),
    gender: Number(form.elements.gender.value),
    phoneNumber: form.elements.phoneNumber.value.trim(),
    email: form.elements.email.value.trim()
  };
  runAction(async () => {
    await request(apiUrl, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(input)
    });
    form.reset(); // Erst nach einem erfolgreichen POST leeren.
    await refreshAfterMutation("Kontakt hinzugefügt.");
  });
});
reload.addEventListener("click", () => runAction(async () => {
  await fetchContacts();
  message("Liste geladen.");
}));
runAction(async () => { await fetchContacts(); message("Liste geladen."); });
