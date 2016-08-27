from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Report)
admin.site.register(Prize)
admin.site.register(ClaimedPrize)
