using AddressBook.Data;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<AddressBookContext>(options => options.UseSqlServer(
    builder.Configuration.GetConnectionString("AddressBook")
        ?? throw new InvalidOperationException("ConnectionStrings:AddressBook fehlt.")));
builder.Services.AddControllers();
builder.Services.AddOpenApi();
builder.Services.AddCors(options => options.AddPolicy("LocalFrontend", policy => policy
    .WithOrigins("http://localhost:5500")
    .AllowAnyHeader().AllowAnyMethod()));

var app = builder.Build();
if (builder.Configuration.GetValue<bool>("ApplyMigrations"))
{
    using var scope = app.Services.CreateScope();
    await scope.ServiceProvider.GetRequiredService<AddressBookContext>().Database.MigrateAsync();
    return;
}
app.UseCors("LocalFrontend");
app.UseDefaultFiles();
app.UseStaticFiles();
if (app.Environment.IsDevelopment()) app.MapOpenApi();
app.MapControllers();
app.Run();

// Ermöglicht Integrationstests mit WebApplicationFactory<Program>.
public partial class Program { }
