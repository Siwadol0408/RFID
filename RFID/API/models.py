from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone


class Tag(models.Model):
    tag_id = models.CharField(max_length=50, primary_key=True)
    tag_name = models.CharField(max_length=30)    
    status = models.TextField(default="อยู่")

class TagHistory(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
    date_time = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='images')