# Generated by Django 4.1.3 on 2023-05-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='languages',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_language', to='accounts.languages'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='typejop',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_time', to='accounts.worktime'),
        ),
    ]