# Generated by Django 4.1.3 on 2023-05-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=models.FileField(default='Course_Certificate_En_Database_Fundamentals.pdf', upload_to='cvProfile/'),
        ),
    ]