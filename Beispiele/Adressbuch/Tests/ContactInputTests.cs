using System.ComponentModel.DataAnnotations;
using AddressBook.Core;
using Xunit;

namespace AddressBook.Tests;

public class ContactInputTests
{
    [Theory]
    [InlineData("", 30, "alice@example.com", "123")]
    [InlineData("   ", 30, "alice@example.com", "123")]
    [InlineData("Alice", -1, "alice@example.com", "123")]
    [InlineData("Alice", 131, "alice@example.com", "123")]
    [InlineData("Alice", 30, "falsch", "123")]
    [InlineData("Alice", 30, "alice@example.com", "")]
    public void InvalidContactIsRejected(string name, int age, string email, string phone)
    {
        var input = new ContactInput { Name = name, Age = age, Email = email, PhoneNumber = phone };
        Assert.False(Validator.TryValidateObject(input, new ValidationContext(input), [], true));
    }

    [Fact]
    public void MappingPreservesTheDatabaseIdAndTrimsText()
    {
        var person = new Person { Id = 42 };
        new ContactInput { Name = " Alice ", Email = " alice@example.com ", PhoneNumber = " 123 " }
            .ApplyTo(person);
        Assert.Equal(42, person.Id);
        Assert.Equal("Alice", person.Name);
        Assert.Equal("alice@example.com", person.Email);
        Assert.Equal("123", person.PhoneNumber);
    }
}
