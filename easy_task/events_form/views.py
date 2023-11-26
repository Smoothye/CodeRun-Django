from django.shortcuts import render, redirect
from .form_models import SeismForm

# Create your views here.
def events_form_view(request):
    
    if request.method == 'POST':
        form = SeismForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list:events_page')
        
    else:
        form = SeismForm()

    return render(request, 'add_form.html', {'form' : form})