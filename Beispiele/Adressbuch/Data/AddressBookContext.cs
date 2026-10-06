using AddressBook.Core;
using Microsoft.EntityFrameworkCore;

namespace AddressBook.Data;

public class AddressBookContext(DbContextOptions<AddressBookContext> options) : DbContext(options)
{
    public DbSet<Person> Contacts => Set<Person>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        var contact = modelBuilder.Entity<Person>();
        contact.ToTable("Contacts", table =>
        {
            table.HasCheckConstraint("CK_Contacts_Age", "[Age] BETWEEN 0 AND 130");
            table.HasCheckConstraint("CK_Contacts_Gender", "[Gender] BETWEEN 0 AND 3");
        });
        contact.Property(p => p.Name).HasMaxLength(100).IsRequired();
        contact.Property(p => p.PhoneNumber).HasMaxLength(50).IsRequired();
        contact.Property(p => p.Email).HasMaxLength(200).IsRequired();
    }
}
