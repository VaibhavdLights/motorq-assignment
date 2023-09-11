from django.urls import path
from .views import upload_document, list_user_documents

urlpatterns = [
     path('', upload_document, name='upload-document'),
     path('documents/', list_user_documents, name='list-user-documents'),
]
