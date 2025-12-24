from django.urls import path
from . import views
from .views import SignUpView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('create/', views.EventCreateView.as_view(), name='event_create'),
    path('<int:id>/', views.EventDetailView.as_view(), name='event_detail'),
    path('<int:pk>/update/', views.EventUpdateView.as_view(), name='event_update'),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name='event_delete'),
    path('<int:id>/participate/', views.EventParticipateView.as_view(), name='event_participate'),
    path('signup/', SignUpView.as_view(template_name='events/signup.html'), name='signup'),
    path('login/', LoginView.as_view(template_name='events/login.html'), name='login'), # тут тоже
    path('logout/', LogoutView.as_view(http_method_names=['get', 'post'], next_page='event_list'), name='logout')
]


