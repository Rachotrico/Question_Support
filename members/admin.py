from django.contrib import admin
from .models import Question



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text","question_image","answer","answer_image"]}),
        ("Date information", 
         {"fields": ["pub_date"], 
          "classes": ["collapse"]}),
    ]
  
admin.site.register(Question,QuestionAdmin)

