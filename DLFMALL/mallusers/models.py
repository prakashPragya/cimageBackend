from django.db import models

class userDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    mobile = models.IntegerField(unique=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

membershipName = (
                    ("silver","Sliver"),
                    ("gold","Gold"),
                    ("Platinum","Platinum")
                )
class membershipDetails(models.Model):
    membershipCategory = models.CharField(max_length=20,choices=membershipName)
    membershipID = models.AutoField(primary_key=True)
    email = models.ForeignKey(userDetails,on_delete=models.CASCADE)
    valdity = models.DateField()

class eventDetails(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=50,unique=True)
    eventDescription = models.DateTimeField(max_length=100)
    eventDate = models.DateTimeField()
    eventVenue = models.CharField(max_length=50)

class registrationDetails(models.Model):
    registrationID = models.AutoField(primary_key=True)
    eventId = models.ForeignKey(eventDetails,on_delete=models.CASCADE)
    email = models.ForeignKey(userDetails,on_delete=models.CASCADE)
