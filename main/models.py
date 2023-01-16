from email.policy import default
from django.db import models
from django.utils import timezone

SERVICE_SERMONS_CHOICES = [
    ('Tuesday Service', 'Tuesday Service'),
    ('Sunday Service', 'Sunday Service'),
]


# Create your models here.
class Sermon(models.Model):
    Service = models.CharField(max_length=200, choices=SERVICE_SERMONS_CHOICES)
    Preacher = models.CharField(max_length=200)
    Date = models.DateField(default=timezone.now)
    Poster = models.ImageField(upload_to="new", blank=True)
    Scripture = models.CharField(max_length=2000)
    Sermon_title = models.CharField(max_length=200)
    Sermon = models.TextField()

    def __str__(self):
        return self.Service

class Activity(models.Model):
    Title = models.CharField(max_length=200)
    Poster = models.ImageField(upload_to="")
    Date = models.DateField(default=timezone.now)
    Venue = models.CharField(max_length=200, default="")
    Description = models.TextField()

    def __str__(self):
        return self.Title

class Family(models.Model):
    Name = models.CharField(max_length=200)
    Leader = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to="new")
    Description = models.TextField()

    def __str__(self):
        return self.Name

class Team(models.Model):
    Name = models.CharField(max_length=200)
    Leader = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to="new")
    Description = models.TextField()

    def __str__(self):
        return self.Name

class Week_Message(models.Model):
    NAME = [
        ('Reverend', 'Reverend'),
        ('Youth Patron', 'Youth Patron'),
        ('Youth Coordinator', 'Youth Coordinator')
    ]
    Name = models.CharField(max_length=200, choices=NAME)
    Message = models.TextField()
    Photo = models.ImageField(upload_to="new")
    Date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.Name

class Payment(models.Model):
    Name = models.CharField(max_length=200)
    Number = models.CharField(max_length=200)
    Purpose = models.CharField(max_length=200)
    Amount = models.IntegerField()
    Paid_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Number

class Schedule(models.Model):
    Name = models.CharField(max_length=200)
    Number = models.IntegerField()
    District = models.CharField(max_length=200)
    Person = models.CharField(max_length=200)
    Date = models.DateField()

    def __str__(self):
        return self.Name

class Membership(models.Model):
    First_name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Number = models.IntegerField()
    Area = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    Confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.First_name

class Booking(models.Model):
    Name = models.CharField(max_length=200)
    Phone_number = models.IntegerField()
    District = models.CharField(max_length=200)
    Activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    Amount = models.IntegerField(default=0)
    Paid = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

class Join_Family(models.Model):
    Name = models.CharField(max_length=200)
    Number = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    # Family = models.ForeignKey(Family, on_delete=models.SET_DEFAULT, default=None)

class Join_Team(models.Model):
    Name = models.CharField(max_length=200)
    Number = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    Team = models.ForeignKey(Team, on_delete=models.SET_DEFAULT, default=None)

class Announcement(models.Model):
     Title = models.CharField(max_length=200)
     Detail = models.TextField()
     Poster = models.ImageField(upload_to="new")
     Date_posted = models.DateTimeField(default=timezone.now)

     def __str__(self):
        return self.Title



   

