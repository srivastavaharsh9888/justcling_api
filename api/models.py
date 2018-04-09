from django.db import models
from django.contrib.auth.models import User

class api_user(models.Model):
	User_Id=models.OneToOneField(User,on_delete=models.CASCADE)
	gender=models.CharField(max_length=8,blank=True)
	address=models.CharField(max_length=50)
	DOB=models.DateField()



