from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', lambda x : redirect('events_form:add_page'), name="homepage"),
    path('add/', include('events_form.urls')),
    path('events/', include('events_list.urls')),
]
