using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Data.Migrations
{
    /// <inheritdoc />
    public partial class ContactConstraints : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddCheckConstraint(
                name: "CK_Contacts_Age",
                table: "Contacts",
                sql: "[Age] BETWEEN 0 AND 130");

            migrationBuilder.AddCheckConstraint(
                name: "CK_Contacts_Gender",
                table: "Contacts",
                sql: "[Gender] BETWEEN 0 AND 3");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropCheckConstraint(
                name: "CK_Contacts_Age",
                table: "Contacts");

            migrationBuilder.DropCheckConstraint(
                name: "CK_Contacts_Gender",
                table: "Contacts");
        }
    }
}
