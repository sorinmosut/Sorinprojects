# Generated by Django 3.0.3 on 2020-11-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0010_mymodel_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='sex',
            field=models.CharField(default='N/A', max_length=1),
        ),
    ]
