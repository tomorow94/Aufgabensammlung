using System.ComponentModel.DataAnnotations;

namespace AddressBook.Core;

// Ein eigener Eingabetyp verhindert, dass Clients Datenbank-IDs vergeben.
public class ContactInput
{
    [Required, StringLength(100)]
    public string Name { get; set; } = "";

    [Range(0, 130)]
    public int Age { get; set; }

    [EnumDataType(typeof(GenderType))]
    public GenderType Gender { get; set; } = GenderType.Unknown;

    [Required, StringLength(50)]
    public string PhoneNumber { get; set; } = "";

    [Required, EmailAddress, StringLength(200)]
    public string Email { get; set; } = "";

    public void ApplyTo(Person person)
    {
        person.Name = Name.Trim();
        person.Age = Age;
        person.Gender = Gender;
        person.PhoneNumber = PhoneNumber.Trim();
        person.Email = Email.Trim();
    }
}
