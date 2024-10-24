from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=25)
    tickets_available = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    cus_name=models.CharField(max_length=20)
    cus_ph=models.CharField(max_length=20)
    title=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    
class Pricing(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.title

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='media/')  
    stars = models.PositiveIntegerField(default=0)  
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user_name} - {self.stars} stars"

