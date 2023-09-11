from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def user_signup(request):
    username = request.data.get('username') 
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(password) < 8:
        return Response({'error':'Password must be 8 or more characters'})
    
    if not any(char.isdigit() for char in password):
        return Response({'error':"The password must contain at least one digit."})
    
    if not any(char.isalpha() for char in password):
        return Response({'error':"The password must contain at least one letter."})
    

    try:
        user = User.objects.get(username=username)
        return Response({'error': 'User with this username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password=password)
        login(request, user) 

        return Response({'message': 'User registered and logged in successfully'}, status=status.HTTP_201_CREATED)
