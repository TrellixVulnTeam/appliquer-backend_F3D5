# Generated by Django 4.0.6 on 2022-08-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_job_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='duration',
            field=models.IntegerField(blank=True),
        ),
    ]
