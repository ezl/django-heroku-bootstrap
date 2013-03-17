from django.contrib import admin

from accounts.models import Patient, Provider

class PatientAdmin(admin.ModelAdmin):
    exclude = ("slug",)

class ProviderAdmin(admin.ModelAdmin):
    exclude = ("slug",)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Provider, ProviderAdmin)
