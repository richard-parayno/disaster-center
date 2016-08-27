from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    exp = models.IntegerField(blank=True,null=True)



    def __str__(self):  
          return "%s's profile" % self.user 

class Reports(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	reportType = models.CharField(max_length=30)
	latitude = models.FloatField()
	longitude = models.FloatField()
	dateTimeStart = models.DateField().auto_now
	dateTimeEnd = models.DateField()



	def __str__(self):
		return 'User: {} {}'.format(self.user.last_name, self.user.first_name)

