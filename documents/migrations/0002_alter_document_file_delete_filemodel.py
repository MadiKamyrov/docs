# Generated by Django 4.2.6 on 2023-10-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='FileModel',
        ),
    ]