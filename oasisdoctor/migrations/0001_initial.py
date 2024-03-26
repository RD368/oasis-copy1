# Generated by Django 5.0.2 on 2024-03-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('workCateg', models.CharField(blank=True, max_length=50)),
                ('workExperience', models.CharField(blank=True, max_length=50)),
                ('workSpecialization', models.CharField(blank=True, max_length=50)),
                ('workLanguage', models.CharField(blank=True, max_length=50)),
                ('doctorAbout', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
