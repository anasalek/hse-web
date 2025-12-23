from django import forms

from .models import Event

# добавляем мероприятие
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description"]
