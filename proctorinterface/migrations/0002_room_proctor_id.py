# Generated by Django 3.0.6 on 2020-06-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proctorinterface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='proctor_id',
            field=models.CharField(default='proctor', max_length=50),
        ),
    ]
