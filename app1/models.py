from django.db import models

# Create your models here.


class employee(models.Model):
    emp_id=models.IntegerField(unique=True,auto_created=True)
    emp_name=models.CharField(max_length=50)
    emp_email=models.EmailField(unique=True)
    emp_salary=models.FloatField()

