from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    english_title = models.CharField(max_length=200)
    english_description = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Booking(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.name} - {self.experience.title}"
