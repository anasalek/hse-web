from django.urls import path

from .views import EventViewset

urlpatterns = [
    path('events/', EventViewset.as_view({"get": "list", "post": "create"})),
    path('events/<int:pk>', EventViewset.as_view({"get": "retrieve"})),
]