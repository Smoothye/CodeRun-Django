from django.shortcuts import render
from events_form.models import Seism

# Create your views here.
def events_list_view(request):

    return render(request, 'events_list.html', {'obj':Seism.objects.all()})
