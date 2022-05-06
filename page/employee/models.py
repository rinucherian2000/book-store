from django.db import models


# Create your models here.

class Employees(models.Model):
    emp_name=models.CharField(max_length=120)
    dept=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField()
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.email


# ORM queries

# CRUD
# Create
# orm query for creating a new Employee
# emp=Employees(emp_name="amal",dept="sales",email="amal@gmail.com",salary=20000,experience=2)
# emp.save()

# Retrieve
# orm queries for listing all employees
# emp=Employees.objects.all()
# emp
#for i in emp:
#   print(i.emp_name,i.dept,i.email,i.salary,i.experience,i.active_status)


# orm filtering
# orm query for listing all employees whoose dept is IT
# emp=Employees.objects.filter(dept="it")
# emp

# orm query for listing all employees whoose experience greater than 1.
# emp=Employees.objects.filter(experience__gt=1)
# emp

# orm query for listing all employees whose salary greater than 15000
# emp=Employees.objects.filter(salary__gt=15000)

# orm query for listing all employees whose salary less than 23000
# emp=Employees.objects.filter(salary__lt=23000)

# orm query for listing all employees whose salary is greater than or equal to 23000.
# emp=Employees.objects.filter(salary__gte=23000)

# orm query for listing all employees whose salary is greater than 21000 but less than 24000.
# emp=Employees.objects.filter(salary__gt=21000,salary__lt=24000)

# orm query for listing all employees whose salary is greater than or equal to 25000 but less than 21000.
# emp=Employees.objects.filter(salary__gte=21000,salary__lt=25000)



# Fetching a specific object
# orm query for fetching a specific record using its id.
# emp=Employees.objects.get(id=3)
# emp





