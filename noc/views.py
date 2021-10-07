import sqlite3

from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
import pandas as pd
import folium
import csv

# Create your views here.
from django.template import loader

from .angle import find_angle
from .arrows import getArrows
from .forms import AddNewAirport, MarkObstruction
from .models import Airport
from .distance import find_distance


def index(request):

    return render(request, 'noc/index.html')

# Add or update airport
def add_airport(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = AddNewAirport()
        else:
            airport = Airport.objects.get(pk=id)
            form = AddNewAirport(instance=airport)
        return render(request, 'noc/add_new_airport.html', {'form': form})
    else:
        if id == 0:
            form = AddNewAirport(request.POST)
        else:
            airport = Airport.objects.get(pk=id)
            form = AddNewAirport(request.POST,instance=airport)
        if form.is_valid():
            form.save()
        return redirect('../../airports')

def delete_airport(request,id):
    airport = Airport.objects.get(pk=id)
    airport.delete()
    return redirect('../../airports')

def airport_list(request):

    csvfile = request.FILES['/home/raghvendra/python_project/airport_data/in-airports.csv']
    filepath = 'noc/in-airports.csv'
    # dataReader = csv.reader(open(filepath), delimiter=',', quotechar='"')
    #
    # for row in dataReader:
    #     airport = Airport()
    #     airport.airport_name = row[0]
    #     airport.save()

    # with open("in-airports.csv",'r') as csvfile:
    con = sqlite3.connect('db.sqlite3')

    pd.read_csv(filepath).to_sql('Airport',con, if_exists='append')
    # You can create your custom dataframe here before converting it to html in next line
    # data_html = data.to_html()
    # context = {'loaded_data': data_html}
    return render(request, 'noc/airports.html')


def airports(request):
    context = {'airport_list': Airport.objects.all()}
    return render(request, 'noc/airport_list.html', context)


def airport_details(request, airport_id):
    if request.method == 'GET':
        form = MarkObstruction()
        try:
            airport = Airport.objects.get(pk=airport_id)
            airport_location = [airport.latitude_deg, airport.longitude_deg]
            map = folium.Map(location=airport_location, control_scale=True)
            ihs = folium.vector_layers.Circle(location=airport_location, fill="red", radius=6100, color="red", opacity=0.4,
                                              popup="IHS", tooltip="IHS")
            ohs = folium.vector_layers.Circle(location=airport_location, fill="blue", radius=20000, color="blue",
                                              opacity=0.4)
            ihs.add_to(map)
            ohs.add_to(map)
            folium.Marker(location=airport_location,
                          popup='ARP %s Elevation: %d Feet' % (airport_location, airport.elevation_ft),
                          tooltip='ARP %s Elevation: %d Feet' % (airport_location, airport.elevation_ft)).add_to(map)
            m = map._repr_html_()
            context: dict = {
                'my_map': m,
                'airport': airport,
                'form':form
            }
        except Airport.DoesNotExist:
            raise Http404("Airport does not exist")
        return render(request, 'noc/airport_details.html', context)
    else:
        airport = Airport.objects.get(pk=airport_id)
        airport_location = [airport.latitude_deg, airport.longitude_deg]
        form = MarkObstruction(request.POST)
        if form.is_valid():
            try:


                obs_latitude = form.cleaned_data['latitude']
                obs_longitude = form.cleaned_data['longitude']
                obstruction = [obs_latitude, obs_longitude]


                dis = find_distance((airport.latitude_deg, airport.longitude_deg), (obs_latitude, obs_longitude))
                angle = find_angle(locations=[airport_location, obstruction])
                print("Radial Distance between Airport and Obstruction is %d deg %f Km " % (angle, dis))

                map = folium.Map(location=airport_location, control_scale=True)
                ihs = folium.vector_layers.Circle(location=airport_location, fill="red", radius=6100, color="red",
                                                  opacity=0.4,
                                                  popup="IHS", tooltip="IHS")
                ohs = folium.vector_layers.Circle(location=airport_location, fill="blue", radius=20000, color="blue",
                                                  opacity=0.4)

                folium.Marker(location=airport_location,
                              popup='ARP %s Elevation: %d Feet' % (airport_location, airport.elevation_ft),
                              tooltip='ARP %s Elevation: %d Feet' % (
                                  airport_location, airport.elevation_ft)).add_to(map)
                folium.Marker(location=obstruction, popup='Obstruction Marker',
                              tooltip="Radial / Distance: %f deg / %f Km" % (angle, dis),
                              icon=folium.Icon(prefix='fa', icon='wifi', color="red")).add_to(map)

                folium.PolyLine(locations=[airport_location, obstruction], color='black',
                                tooltip="Radial / Distance: %f deg / %f Km" % (angle, dis)).add_to(map)
                arrows = getArrows(locations=[airport_location, obstruction], n_arrows=1)
                for arrow in arrows:
                    arrow.add_to(map)

                ihs.add_to(map)
                ohs.add_to(map)

                m = map._repr_html_()
                context: dict = {
                    'my_map': m,
                    'airport': airport,
                    'form': form
                }
            except Airport.DoesNotExist:
                raise Http404("Airport does not exist")
            return render(request, 'noc/airport_details.html', context)

def plot_route(request) :
    return render(request, 'noc/template.html')

def mark_obstruction(request):
    return render(request, 'noc/template.html')


