# Generated by Django 4.2.4 on 2023-09-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0005_remove_employee_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Email',
            field=models.EmailField(max_length=25),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
