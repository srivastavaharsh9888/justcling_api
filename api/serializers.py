from rest_framework import serializers
from .models import api_user
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

	class Meta(object):
		model=User
		fields=['first_name','last_name','username']
		read_only_fields=['first_name','last_name','username']



class api_userSerializer(serializers.ModelSerializer):
		User_Id=UserSerializer()
		class Meta(object):
			model = api_user	
			fields='__all__'
			read_only_fields=['User_Id','address','DOB',]

		
		
