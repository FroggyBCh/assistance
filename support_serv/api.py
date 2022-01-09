from .models import Problem, Message
from rest_framework import viewsets, permissions
from .serializers import ProblemSerializer, MessageSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProblemSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MessageSerializer