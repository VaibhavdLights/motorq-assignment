from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name', 'document_id', 'data')

class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name', 'document_id')
