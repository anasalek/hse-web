from rest_framework import serializers

from Events.models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ("name", "description")
        extra_kwargs = {
            'organizer': {'required': False}
        }
