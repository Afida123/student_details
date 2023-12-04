from django.db import models


# Create your models here.
class Employee(models.Model):
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.uname

class Student(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.place
    def __str__(self):
        return self.email
    def __str__(self):
        return self.age
    
class emp(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=30)

class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)

    def __str__(self):
      return self.title

class Person(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    course=models.CharField(max_length=30)

class Mobiles(models.Model):
    name=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    
    launch_year=models.CharField(max_length=20)


class Students(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveBigIntegerField()
    course=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    place=models.CharField(max_length=30)

    def __str__(self):
         return f"{self.name} {self.age} {self.course} {self.gender} {self.place}"
   








