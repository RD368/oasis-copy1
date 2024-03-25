# Generated by Django 5.0.2 on 2024-03-25 14:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasisauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pdf_files/')),
                ('uploadedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateTimeField(null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('bloodGroup', models.CharField(blank=True, max_length=30)),
                ('height', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('bmi', models.FloatField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pdf_files', models.ManyToManyField(blank=True, related_name='patient_records', to='oasisauth.pdffiles')),
            ],
        ),
    ]
