# Generated by Django 5.0.3 on 2024-03-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0004_patient_details_dob_patient_details_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_details',
            name='phone_number',
            field=models.CharField(default=0, max_length=12),
        ),
    ]
