from django.urls import path
from . import views

app_name = 'events_list'

urlpatterns = [
    path('', views.events_list_view, name = "events_page")
]
