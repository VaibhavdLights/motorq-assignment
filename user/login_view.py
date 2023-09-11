from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
