from django.contrib import admin
from .models import department, Role, employee

admin.site.register(department)
admin.site.register(Role)
admin.site.register(employee)
