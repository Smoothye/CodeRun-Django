from .models import Seism
from django.forms import ModelForm

class SeismForm(ModelForm):
    class Meta:
        model = Seism
        fields = ["start_time", "end_time", "magnitude", "depth", "longitude", "latitude"]