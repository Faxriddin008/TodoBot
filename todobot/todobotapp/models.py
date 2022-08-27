from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    completed = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(on_delete=models.CASCADE)
