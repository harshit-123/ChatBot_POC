from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class UploadPDF(models.Model):
    pdf = models.FileField(upload_to='pdf/', validators=[FileExtensionValidator( ['pdf'] ) ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)