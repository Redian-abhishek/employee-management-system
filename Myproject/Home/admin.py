from django.contrib import admin
from . models import Employee
# Register your models here.

class admin_employee(admin.ModelAdmin):
    list_display=('eid','ename','eemail','econtact','edept','ecity')
    search_fields = ('eid','ename','eemail','econtact','edept','ecity')
    list_filter = ('ename', 'edept','ecity')
    list_per_page = 20 
    list_display_links =('eid','ename','eemail','econtact','edept','ecity')
    def __str__(self):
        return self.name

admin.site.register(Employee,admin_employee)