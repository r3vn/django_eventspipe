# Generated by Django 5.1.1 on 2024-09-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_eventspipe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='pipelineartifact',
            name='file_name',
            field=models.CharField(default='undefined', max_length=1024),
        ),
        migrations.AddField(
            model_name='pipelineartifact',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
