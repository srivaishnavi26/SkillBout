from django.db import models
class Employee(models.Model):
    employee_type_choices = [
        ('Full time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField()
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    date_of_hire = models.DateField()
    employment_type = models.CharField(max_length=20, choices=employee_type_choices)
    address = models.CharField(max_length=100)
    active_status = models.BooleanField()
    def __str__(self):
        return self.name