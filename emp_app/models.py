from django.db import models

# Create your models here.

class Employee(models.Model):
    First_name = models.CharField(max_length=10)
    Last_name = models.CharField(max_length=10)
    Dept = models.CharField(max_length=10)
    Salary = models.IntegerField(default=0)
    Role = models.CharField(max_length=20)
    phone = models.CharField(max_length=20,default=0)
    hire_date = models.DateField()
    def __str__(self):
        return "%s %s" % (self.First_name, self.Last_name)

    class Meta:
        db_table = "office"
