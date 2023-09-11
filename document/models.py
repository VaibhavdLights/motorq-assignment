import uuid
from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    document_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    data = models.JSONField()