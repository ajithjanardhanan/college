from django.db import models


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_url = models.URLField()

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=100)
    materials_provide = models.CharField(max_length=100)

    def __str__(self):
        return self.name


