from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from user_app import models

@api_view(["POST",])
def logout_view(request):
    if request.method=="POST":
        request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["POST",])
def register_view(request):
    if request.method=="POST":
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            
            
            data["response"]="Registration sucessful !!!"
            data["username"]=account.username
            data["email"]=account.email
            
            token,created=Token.objects.get_or_create(user=account)
            data["account"]=token.key
            
        else:
            data=serializer.errors
            
        return Response(data,status=status.HTTP_201_CREATED)
        