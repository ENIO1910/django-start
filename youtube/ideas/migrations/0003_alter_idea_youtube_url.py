# Generated by Django 5.1.7 on 2025-03-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_alter_idea_youtube_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
