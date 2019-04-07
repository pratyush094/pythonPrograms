from django.contrib import admin
from .models import Admin, Donor, Organisation

admin.site.register(Admin)
admin.site.register(Donor)
admin.site.register(Organisation)
