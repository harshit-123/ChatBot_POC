from django.db import models

# Create your models here.
class TrainModel(models.Model):
    pdf_path = models.CharField(max_length=100, default='media/pdf')
    input_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class TrainModelDB(models.Model):
    input_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)