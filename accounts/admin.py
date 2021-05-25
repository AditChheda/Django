from django.contrib import admin
from .models import AccountDatabase, UserInformation, CollegeName
# Register your models here.
@admin.register(AccountDatabase)
class AccountDatabaseAdmin(admin.ModelAdmin):
    list_display = ("FirstName", "LastName", "Username", "Email")

@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ("College", "CollegeAddress", "AcademicYear", "Department", "Division", "RollNo")

admin.site.register(CollegeName)
