# Generated by Django 5.1.3 on 2024-11-09 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
