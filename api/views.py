from django.shortcuts import redirect
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import api_userSerializer
from .models import api_user
from django.contrib.auth.models import User
from django.http import JsonResponse

class show(generics.RetrieveAPIView):

	lookup_field='pk'
	serializer_class=api_userSerializer

	def get_queryset(self):
		return api_user.objects.all()

		
class update(generics.CreateAPIView):

	serializer_class=api_userSerializer

	def post(self,request,*args,**kwargs):
		USER_obj=api_user.objects.filter(pk=self.kwargs.get("pk"))	
		if len(USER_obj)!=0:
			value=str(self.request.data.get("gender"))
			if value.lower()=="female":
				value= "Female"
			if value.lower()=="male":
				value= "Male"
			if value.lower()=="other":
				value= "Other"
			if value=="Female" or value=="Male" or value=="Other":
				USER_obj.update(gender=value)
				username=USER_obj[0].User_Id.username
				return Response({"Success":"Done","data":[username,USER_obj[0].gender]})
			else:
				return Response({"Error":"Please Enter only Male, Female or Other"})
		else:
			return Response({"Error":"No User with such Id exists."})
		





