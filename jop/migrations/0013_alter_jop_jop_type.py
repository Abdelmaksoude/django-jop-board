# Generated by Django 4.1.3 on 2023-02-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0012_alter_jop_jop_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jop',
            name='Jop_Type',
            field=models.CharField(max_length=15),
        ),
    ]
