# Generated by Django 4.1.3 on 2023-06-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0041_remove_apply_cv_remove_apply_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]