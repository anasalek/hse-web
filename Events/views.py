from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Event, Participation
from Events.forms import EventForm
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView


class EventCreateView(CreateView):
    """Создание нового события"""
    model = Event
    form_class = EventForm
    template_name = "events/event_create.html" 
    pk_url_kwarg = "id"
    template_name_suffix = "_create"
    success_url = reverse_lazy("event_list")
    def form_valid(self, form):
        form.instance.organizer = self.request.user 
        return super().form_valid(form)
    
class EventDetailView(DetailView):
    """Детальная информация о событии"""
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"
    pk_url_kwarg = "id"

class EventListView(ListView):
    """Список всех событий"""
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"

class EventUpdateView(UpdateView):
    """Редактирование события"""
    model = Event
    form_class = EventForm
    template_name = "events/event_update.html"
    context_object_name = "event"
    pk_url_kwarg = "id"
    template_name_suffix = "_update"
    success_url = reverse_lazy("events/event_list")

class EventDeleteView(DeleteView):
    """Удаление события"""
    model = Event
    template_name = "event/event_delete.html" 
    context_object_name = "event"
    pk_url_kwarg = "id"
    template_name_suffix = "_delete"
    success_url = reverse_lazy("events/event_list")

    
class EventParticipateView(LoginRequiredMixin, View):
    """Запись на событие"""
    login_url = reverse_lazy('/login')  # если не залогинились, редирект на страницу входа
    success_url = reverse_lazy('events/event_list') # если вошли в аккаунт, редирект на список мероприятий
    
    def post(self, request, id):
        event = get_object_or_404(Event, id=id)
        
        # проверяем, не записан ли уже пользователь
        participation, created = Participation.objects.get_or_create(
            participant=request.user,
            event=event
        )
        
        if created:
            messages.success(request, f'Вы успешно записались на событие "{event.name}"')
        else:
            messages.info(request, f'Вы уже записаны на событие "{event.name}"')
        
        return redirect('event_detail', id=event.id)
    
class SignUpView(CreateView):
        '''Зарегестрироваться'''
        form_class = SignUpForm
        success_url = reverse_lazy('/login') # при успешной регистрации редирект на логин
        template_name = '/signup.html' # здесь не уверена в пути