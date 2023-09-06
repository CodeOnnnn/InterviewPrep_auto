
from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
import uuid
# Create your models here.
class Question(models.Model):
    author= models.ForeignKey(User,null=False, on_delete=models.CASCADE)
    title=models.CharField(max_length=200, null=False)
    body= models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    max_score=models.FloatField(default=100)
    def __str__(self):
        return self.title
    
class Response(models.Model):
    user=models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    # record=models.FileField(upload_to='documents/')
    parent=models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE)
    body=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voice_record = models.FileField(upload_to="records")
    language = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("record_detail", kwargs={"id": str(self.id)})

    def __str__(self):
        return self.body
    
    