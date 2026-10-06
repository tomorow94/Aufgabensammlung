namespace AddressBook.Core;

public enum GenderType { Unknown, Male, Female, Diverse }

public class Person
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public int Age { get; set; }
    public GenderType Gender { get; set; } = GenderType.Unknown;
    public string PhoneNumber { get; set; } = "";
    public string Email { get; set; } = "";

    public override string ToString() => $"{Id}: {Name}, {Age}, {PhoneNumber}, {Email}";
}
