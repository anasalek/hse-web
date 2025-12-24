from rest_framework import viewsets
from Events.models import Event
from .serializers import EventSerializer

class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        """Указывает текущего пользователя как организатора"""
        user = self.request.user
        serializer.save(organizer=user)