# Generated by Django 4.1.3 on 2023-02-06 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0007_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='jop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply_jop', to='jop.jop'),
            preserve_default=False,
        ),
    ]