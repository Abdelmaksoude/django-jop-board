# Generated by Django 4.1.3 on 2023-03-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0014_alter_jop_jop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='place',
            field=models.CharField(choices=[('Menofia', 'Menofia'), ('Cairo', 'Cairo'), ('Giza', 'Giza'), ('Tanta', 'Tanta'), ('Mansora', 'Mansora'), ('Kafr Elshek', 'Kafr Elshek'), ('6 Octper', 'Menofia')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
