# Generated by Django 4.2.4 on 2023-08-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Role',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=0, max_length=20),
        ),
    ]