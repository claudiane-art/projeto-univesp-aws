# Generated by Django 5.1.1 on 2024-09-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_files_doc_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='doc_type',
            field=models.CharField(default='other', max_length=30),
        ),
    ]