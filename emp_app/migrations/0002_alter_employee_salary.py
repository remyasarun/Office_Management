# Generated by Django 4.2.3 on 2023-08-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
    ]
