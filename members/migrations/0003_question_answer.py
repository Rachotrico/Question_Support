# Generated by Django 5.1.3 on 2024-11-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_question_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
