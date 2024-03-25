from django.contrib import admin
from .models import CustomUser,PatientRecord,PdfFiles
# Register your models here.)

admin.site.register(CustomUser),
admin.site.register(PatientRecord),
admin.site.register(PdfFiles)