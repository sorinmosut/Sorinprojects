# Generated by Django 3.0.3 on 2020-11-03 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_mymodel_no_tel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='no_tel',
        ),
    ]
