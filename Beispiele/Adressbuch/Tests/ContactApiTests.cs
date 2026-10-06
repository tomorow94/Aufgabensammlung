using System.Net;
using System.Net.Http.Json;
using AddressBook.Core;
using AddressBook.Data;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.Data.Sqlite;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;
using Xunit;

namespace AddressBook.Tests;

// Jede Testmethode erstellt einen eigenen Host und eine eigene relationale Datenbank.
public class ContactApiFactory : WebApplicationFactory<Program>
{
    private readonly SqliteConnection connection = new("Data Source=:memory:");

    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        connection.Open();
        builder.UseEnvironment("Testing");
        builder.ConfigureServices(services =>
        {
            services.RemoveAll<AddressBookContext>();
            services.RemoveAll<DbContextOptions<AddressBookContext>>();
            services.RemoveAll<IDbContextOptionsConfiguration<AddressBookContext>>();
            services.AddDbContext<AddressBookContext>(options => options.UseSqlite(connection));
        });
    }

    public HttpClient CreateInitializedClient()
    {
        var client = CreateClient();
        using var scope = Services.CreateScope();
        scope.ServiceProvider.GetRequiredService<AddressBookContext>().Database.EnsureCreated();
        return client;
    }

    protected override void Dispose(bool disposing)
    {
        base.Dispose(disposing);
        if (disposing) connection.Dispose();
    }
}

public class ContactApiTests
{
    private static ContactInput ValidInput(string name = "Alice") => new()
    {
        Name = name, Age = 30, Gender = GenderType.Unknown,
        PhoneNumber = "012345", Email = "alice@example.com"
    };

    [Fact]
    public async Task CreateReadUpdateAndDeletePersistTheContact()
    {
        using var factory = new ContactApiFactory();
        using var client = factory.CreateInitializedClient();
        var create = await client.PostAsJsonAsync("/api/contacts", ValidInput());
        Assert.Equal(HttpStatusCode.Created, create.StatusCode);
        var person = (await create.Content.ReadFromJsonAsync<Person>())!;
        Assert.True(person.Id > 0);
        Assert.EndsWith($"/api/contacts/{person.Id}", create.Headers.Location!.ToString());
        var read = (await client.GetFromJsonAsync<Person>($"/api/contacts/{person.Id}"))!;
        Assert.Equal("Alice", read.Name);
        var update = await client.PutAsJsonAsync($"/api/contacts/{person.Id}", ValidInput("Bob"));
        Assert.Equal(HttpStatusCode.NoContent, update.StatusCode);
        Assert.Equal("Bob", (await client.GetFromJsonAsync<Person>($"/api/contacts/{person.Id}"))!.Name);
        Assert.Equal(HttpStatusCode.NoContent, (await client.DeleteAsync($"/api/contacts/{person.Id}")).StatusCode);
        Assert.Equal(HttpStatusCode.NotFound, (await client.GetAsync($"/api/contacts/{person.Id}")).StatusCode);
    }

    [Fact]
    public async Task DeletingAndAddingDoesNotReuseAnExistingId()
    {
        using var factory = new ContactApiFactory();
        using var client = factory.CreateInitializedClient();
        async Task<Person> Add(string name)
        {
            var response = await client.PostAsJsonAsync("/api/contacts", ValidInput(name));
            response.EnsureSuccessStatusCode();
            return (await response.Content.ReadFromJsonAsync<Person>())!;
        }
        var first = await Add("First");
        var second = await Add("Second");
        await client.DeleteAsync($"/api/contacts/{first.Id}");
        var third = await Add("Third");
        Assert.NotEqual(second.Id, third.Id);
        var contacts = (await client.GetFromJsonAsync<List<Person>>("/api/contacts"))!;
        Assert.Equal(2, contacts.Count);
        Assert.Equal(2, contacts.Select(p => p.Id).Distinct().Count());
    }

    [Theory]
    [InlineData("{}")]
    [InlineData("{\"name\":\"Alice\",\"phoneNumber\":\"123\"}")]
    [InlineData("{\"name\":\"Alice\",\"phoneNumber\":\"123\",\"email\":\"invalid\"}")]
    [InlineData("{\"name\":\"Alice\",\"phoneNumber\":\"123\",\"email\":\"alice@example.com\",\"gender\":99}")]
    public async Task InvalidRequestReturns400WithoutWritingData(string json)
    {
        using var factory = new ContactApiFactory();
        using var client = factory.CreateInitializedClient();
        var response = await client.PostAsync("/api/contacts",
            new StringContent(json, System.Text.Encoding.UTF8, "application/json"));
        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
        Assert.Empty((await client.GetFromJsonAsync<List<Person>>("/api/contacts"))!);
    }

    [Fact]
    public async Task MissingContactsReturn404ForAllSingleContactOperations()
    {
        using var factory = new ContactApiFactory();
        using var client = factory.CreateInitializedClient();
        Assert.Equal(HttpStatusCode.NotFound, (await client.GetAsync("/api/contacts/999")).StatusCode);
        Assert.Equal(HttpStatusCode.NotFound, (await client.PutAsJsonAsync("/api/contacts/999", ValidInput())).StatusCode);
        Assert.Equal(HttpStatusCode.NotFound, (await client.DeleteAsync("/api/contacts/999")).StatusCode);
    }

    [Fact]
    public async Task SeparateLocalFrontendCanSendJsonRequests()
    {
        using var factory = new ContactApiFactory();
        using var client = factory.CreateInitializedClient();
        using var request = new HttpRequestMessage(HttpMethod.Options, "/api/contacts");
        request.Headers.Add("Origin", "http://localhost:5500");
        request.Headers.Add("Access-Control-Request-Method", "POST");
        request.Headers.Add("Access-Control-Request-Headers", "content-type");
        var response = await client.SendAsync(request);
        Assert.Equal(HttpStatusCode.NoContent, response.StatusCode);
        Assert.Equal("http://localhost:5500", Assert.Single(response.Headers.GetValues("Access-Control-Allow-Origin")));
    }
}
