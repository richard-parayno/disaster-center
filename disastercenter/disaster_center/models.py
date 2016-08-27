from django.db import models
from django.contrib.auth.models import User
import datetime


class UserProfile(models.Model):

    user = models.CharField(max_length=15, default="default")
    password=models.CharField(max_length=15, default="p@ssword")
    email = models.CharField(max_length=30,default="default@gmail.com")
    first_name = models.CharField(max_length=30,default="default")
    last_name = models.CharField(max_length=30,default="default")
    exp = models.IntegerField(default=0)
    points = models.IntegerField(default=0)



    def __str__(self):
          return "%s's profile" % self.user

class Report(models.Model):
	types = (
        ('Flood','Flood'),
        ('Traffic','Traffic'),
        ('LandSlide','LandSlide'),
        ('Road Accident','Road Accident'),
        ('Fire Alert','Fire Alert')
    )
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	reportType = models.CharField(max_length=30, choices=types)
	latitude = models.FloatField()
	longitude = models.FloatField()
	dateTimeStart = models.DateTimeField(null=True)
	dateTimeEnd = models.DateTimeField(null=True, blank=True)



	def __str__(self):
		return 'User: {} {}'.format(self.user.last_name, self.user.first_name)

class Prize(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,default=0)
	name = models.CharField(max_length=30,default="default")
	pointCost = models.IntegerField(default=0)
	code = models.CharField(max_length=30,default="default")
	taken = models.BooleanField(default=False)
	claimed =models.BooleanField(default=False)


	def __str__(self):
		return 'User: {} {}'.format(self.user.last_name, self.user.first_name)

class ClaimedPrize(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	prize = models.ForeignKey(Prize,on_delete=models.CASCADE)
	def __str__(self):
		return 'User: {} {}'.format(self.user.last_name, self.user.first_name)
