from django.db import models
from datetime import datetime

# Create your models here.
class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField(default=datetime.now)
    qualification = models.CharField(max_length=20)
    tech_skills = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=50)

    # return concatenated name
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    
