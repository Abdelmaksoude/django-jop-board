# Generated by Django 4.1.3 on 2023-03-28 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0025_alter_comment_content_alter_comment_jop_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]