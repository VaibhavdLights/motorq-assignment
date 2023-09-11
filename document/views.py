from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentListSerializer, DocumentSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_document(request):
    user = request.user
    data = request.data

    serializer = DocumentSerializer(data=data)
    if serializer.is_valid():
        name = serializer.validated_data['name']

        if Document.objects.filter(name=name, owner=user).exists():
            return Response({'error': 'A document with this name already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'data' not in data or not isinstance(data['data'], dict) or not data['data']:
            return Response({'error': 'The "data" field must be a non-empty JSON object.'}, status=status.HTTP_400_BAD_REQUEST)

        
        document = Document(name=name, owner=user, data=data['data'])
        document.save()

        return Response({'document_id': document.document_id}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_documents(request):
    user = request.user
    documents = Document.objects.filter(owner=user)
    serializer = DocumentListSerializer(documents, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
