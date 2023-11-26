from django.urls import path
from . import views

app_name = 'events_form'

urlpatterns = [
    path('', views.events_form_view, name="add_page")
]
