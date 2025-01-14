# Generated by Django 5.0.1 on 2024-03-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='document_type',
            field=models.CharField(blank=True, choices=[('CPF', 'CPF'), ('RG', 'RG'), ('PASSAPORTE', 'Passaporte'), ('SSN', 'Social Security Number')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='document_value',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('document_type', 'document_value')},
        ),
    ]
