# Generated by Django 4.2.4 on 2023-09-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_alter_employee_role_alter_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Email',
            field=models.EmailField(default=0, max_length=25),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='password2',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
