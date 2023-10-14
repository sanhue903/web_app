from django.db import models

# Create your models here.

class Student(models.Model):
    first_name       = models.CharField(
        max_length=50,
        blank=False
    )
    last_name        = models.CharField(
        max_length=50, 
        blank=False
    )
    
    second_last_name = models.CharField(
        max_length=50,
        blank=False
    )
    
    age              = models.IntegerField(null=False)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class App(models.Model):
    name        = models.CharField(
        max_length=50, 
        blank=False
    )
    
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Module(models.Model):
    name        = models.CharField(
        max_length=50, 
        blank=False
    )
    description = models.TextField()
    app         = models.ForeignKey(
        App, 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name
    
class Score(models.Model):
    attempts = models.IntegerField(null=False)
    duration = models.DurationField(null=False)
    
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE,
        null=False
    )
    
    module = models.ForeignKey(
        Module, 
        on_delete=models.CASCADE,
        null=False
    )
    
    def __str__(self):
        return str(id)