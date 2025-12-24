from django import forms
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# добавляем мероприятие
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description"]

# регистрация пользователей
class SignUpForm(UserCreationForm):
    user_name = forms.CharField(max_length=30, required=True, help_text="Обязательно")
    first_name = forms.CharField(max_length=30, required=False, help_text="Опционально")
    last_name = forms.CharField(max_length=30, required=False, help_text="Опционально")
    email = forms.EmailField(max_length=254, help_text="Введите email")

    class Meta:
        model=User
        fields = [
            'user_name',
            'first_name',
            'last_name',
            'email'
        ]

