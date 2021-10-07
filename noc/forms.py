from django.forms import ModelForm

from .models import Airport, Obstruction


class AddNewAirport(ModelForm):
   class Meta:
    model = Airport
    fields = '__all__'


class MarkObstruction(ModelForm):
   class Meta:
    model = Obstruction
    fields = '__all__'


