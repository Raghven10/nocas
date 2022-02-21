from django.forms import ModelForm

from .models import Airport, Obstruction, Area, Point


class AddNewAirport(ModelForm):
   class Meta:
    model = Airport
    fields = '__all__'


class MarkObstruction(ModelForm):
   class Meta:
    model = Obstruction
    fields = '__all__'

class MarkAreaForm(ModelForm):
   class Meta:
    model = Area
    fields = '__all__'


class PointForm(ModelForm):
   class Meta:
    model = Point
    fields = '__all__'