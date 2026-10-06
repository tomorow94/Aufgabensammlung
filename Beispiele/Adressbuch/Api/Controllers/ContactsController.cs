using AddressBook.Core;
using AddressBook.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace AddressBook.Api.Controllers;

[ApiController]
[Route("api/contacts")]
public class ContactsController(AddressBookContext context) : ControllerBase
{
    [HttpGet]
    public async Task<ActionResult<List<Person>>> GetAll() =>
        await context.Contacts.AsNoTracking().OrderBy(p => p.Name).ToListAsync();

    [HttpGet("{id:int}")]
    public async Task<ActionResult<Person>> GetById(int id)
    {
        var contact = await context.Contacts.FindAsync(id);
        return contact is null ? NotFound() : Ok(contact);
    }

    [HttpPost]
    public async Task<ActionResult<Person>> Create(ContactInput input)
    {
        var contact = new Person();
        input.ApplyTo(contact);
        context.Contacts.Add(contact);
        await context.SaveChangesAsync();
        return CreatedAtAction(nameof(GetById), new { id = contact.Id }, contact);
    }

    [HttpPut("{id:int}")]
    public async Task<IActionResult> Update(int id, ContactInput input)
    {
        var contact = await context.Contacts.FindAsync(id);
        if (contact is null) return NotFound();
        input.ApplyTo(contact);
        await context.SaveChangesAsync();
        return NoContent();
    }

    [HttpDelete("{id:int}")]
    public async Task<IActionResult> Delete(int id)
    {
        var contact = await context.Contacts.FindAsync(id);
        if (contact is null) return NotFound();
        context.Contacts.Remove(contact);
        await context.SaveChangesAsync();
        return NoContent();
    }
}
