# Generated by Django 4.1.3 on 2023-02-05 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jop.category'),
            preserve_default=False,
        ),
    ]