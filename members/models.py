import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.db.models.functions import Now

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(db_default=Now())
    question_image = models.ImageField(null=True,blank=True,upload_to="images/")
    answer = models.CharField(null=True,max_length=1000)
    answer_image = models.ImageField(null=True,blank=True,upload_to="images_answer/")
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
