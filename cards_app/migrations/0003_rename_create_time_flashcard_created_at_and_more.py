# Generated by Django 5.1.6 on 2025-03-01 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards_app', '0002_flashcard_create_time_flashcard_update_time_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flashcard',
            old_name='create_time',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='flashcard',
            old_name='update_time',
            new_name='updated_at',
        ),
    ]
