# Generated by Django 4.1.3 on 2023-06-20 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0042_apply_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='slug',
        ),
    ]