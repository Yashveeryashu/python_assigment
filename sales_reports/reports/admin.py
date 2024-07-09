from django.contrib import admin

# Register your models here.
from .models import RawData,ProcessedData,EmailAddress

admin.site.register(RawData)
admin.site.register(ProcessedData)
admin.site.register(EmailAddress)