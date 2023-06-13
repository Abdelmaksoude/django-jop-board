# Generated by Django 4.1.3 on 2023-03-27 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jop', '0018_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='jop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='jop.jop'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]