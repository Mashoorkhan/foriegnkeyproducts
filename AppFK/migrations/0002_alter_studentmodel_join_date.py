# Generated by Django 3.2.13 on 2022-09-13 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFK', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='Join_Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
