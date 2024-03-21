# views.py
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # Use ReadOnlyModelViewSet para listar e visualizar detalhes
    queryset = User.objects.all()
    serializer_class = UserSerializer
