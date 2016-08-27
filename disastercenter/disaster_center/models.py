from django.db import models
from django.contrib.auth.models import User
import datetime


class UserProfile(models.Model):  

    user = models.OneToOneField(User)  
    email = models.CharField(max_length=30,default="default@gmail.com")  
    first_name = models.CharField(max_length=30,default="default")  
    last_name = models.CharField(max_length=30,default="default")  
    exp = models.IntegerField(default=0)
    points = models.IntegerField(default=0)



    def __str__(self):  
          return "%s's profile" % self.user 

class Report(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	reportType = models.CharField(max_length=30)
	latitude = models.FloatField()
	longitude = models.FloatField()
	dateTimeStart = models.DateTimeField(null=True)
	dateTimeEnd = models.DateTimeField(null=True, blank=True)



	def __str__(self):
		return 'User: {} {}'.format(self.user.last_name, self.user.first_name)

