from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    user_data = [{'username': user.username} for user in users]
    return Response(user_data, status=status.HTTP_200_OK)
