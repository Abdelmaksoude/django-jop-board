# Generated by Django 4.1.3 on 2023-04-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0036_remove_comment_content_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
