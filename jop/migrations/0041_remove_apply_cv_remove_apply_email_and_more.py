# Generated by Django 4.1.3 on 2023-06-20 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jop', '0040_apply_cv_apply_email_apply_website_alter_apply_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='email',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='website',
        ),
        migrations.AlterField(
            model_name='apply',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_apply_jop', to=settings.AUTH_USER_MODEL),
        ),
    ]
