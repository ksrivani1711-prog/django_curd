from django.contrib import admin

from app1.models import employee

class Employee_admin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_email','emp_salary']
    ordering=['emp_id']
admin.site.register(employee,Employee_admin)
