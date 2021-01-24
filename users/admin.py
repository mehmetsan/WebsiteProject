from django.contrib import admin
from .models import  Employee


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('first_name', 'last_name', 'position',)
    list_filter = ('full_name',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name','full_name', 'position', 'phone', 'email' , 'picture', 'linked_In_URL' )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','first_name', 'last_name','linked_In_URL', 'position')}
        ),
    )
    search_fields = ('full_name',)
    ordering = ('full_name',)

admin.site.register(Employee, EmployeeAdmin)