from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    email = models.CharField(max_length=30,default="default@gmail.com")  
    first_name = models.CharField(max_length=30,default="default")  
    last_name = models.CharField(max_length=30,default="default")  
    exp = models.IntegerField(default=0)



    def __str__(self):  
          return "%s's profile" % self.user 

class Report(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	reportType = models.CharField(max_length=30)
	latitude = models.FloatField()
	longitude = models.FloatField()
	dateTimeStart = models.DateField().auto_now
	dateTimeEnd = models.DateField(default="00/00/00").auto_now



	def __str__(self):
		return 'User: {} {}'.format(self.user.last_name, self.user.first_name)

