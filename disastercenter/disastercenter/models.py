from django.db import models
from django.contrib.auth.models import User

class Reports(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	reportType = models.CharField(max_length=30)
	latitude = models.LongField()
	longitude = models.LongField()
	dateTimeStart = models.DateField().auto_now
	dateTimeEnd = models.DateField()



	def __str__(self):
		return 'User: {} {}'.format(self.user.last_name, self.user.first_name)
