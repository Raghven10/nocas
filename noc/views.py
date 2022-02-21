import sqlite3

from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
import pandas as pd
import folium
import csv

# Create your views here.
from django.template import loader

from noc.my_map import draw_area, show_map

from .angle import find_angle
from .arrows import getArrows
from .forms import AddNewAirport, MarkAreaForm, MarkObstruction, PointForm
from .models import Airport, Area, Point
from .distance import find_distance


def index(request):
    airport_location = [28.5665, 77.103104] # IGI Airport Delhi location
    demo_map = folium.Map(location=airport_location, control_scale=True, zoom_start=10)
    folium.Marker(location=airport_location).add_to(demo_map)

    my_map = demo_map._repr_html_()
    context = {
        'my_map':my_map
    }

    return render(request, 'noc/index.html',context)

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
            areas = Area.objects.all()
            for area in areas:
                points = Point.objects.filter(area=area.id)
                if len(points) == 0:
                    pass
                else:
                    coordinates = []                
                    for p in points:
                        coordinate = (p.latitude, p.longitude)

                        div = folium.DivIcon(html=(
                        '<svg height="100" width="200">'                        
                        '<text x="10" y="10" fill="black">%s</text>'
                        '</svg>'% ([p.point_name,  p.latitude,    p.longitude])
                        ))

                        folium.Marker([p.latitude, p.longitude],icon=div).add_to(map)
                        
                        coordinates.append(coordinate)
                    shapesLayer = folium.FeatureGroup(name=area.name).add_to(map)    
                    folium.Polygon(locations=coordinates, color=area.color, fill_color  = area.fill_color, tooltip=area.name).add_to(shapesLayer)
            folium.LayerControl().add_to(map)  
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

def area_plot(request) :
    if request.method == 'GET':
        form = MarkAreaForm()
        try:

            airport_location = [28.5665, 77.103104] # IGI Airport Delhi location
            map = folium.Map(location=airport_location, control_scale=True, zoom_start=10)

            for airport in Airport.objects.all():
                airport_location = [airport.latitude_deg, airport.longitude_deg]
                ihs = folium.vector_layers.Circle(location=airport_location, fill="red", radius=5000, color="red", opacity=0.4,
                                              popup="5KM Radius", tooltip="5KM Radius")
                ihs.add_to(map)
                folium.Marker(location=airport_location,
                          popup='%s %s ARP %s ' % (airport.name, airport.ident, airport_location),
                          tooltip='%s ' % (airport.name)).add_to(map)
                
           
            # create a layer on the map object
            
            shapesLayer = folium.FeatureGroup(name="Exercise Area").add_to(map)          
           

            # create a polygon with the coordinates
            folium.Polygon([(12.37, 77.58), (11.48, 79.46), (11.09, 78.53),
                 (11.27, 77.52)],
                color="red",
                fill_color="orange",
                weight=2).add_to(shapesLayer)
            folium.LayerControl().add_to(map)
            
            m = map._repr_html_()
            context: dict = {
                'my_map': m,                
                'form':form
            }
        except Airport.DoesNotExist:
            raise Http404("Airport does not exist")
        return render(request, 'noc/area_plot.html', context)
    else:
        form = MarkAreaForm(request.POST)
        if form.is_valid:
           area =  form.save()  
           

        return redirect('point_plot',id=area.id)


def point_plot(request, id):
    if request.method == 'GET':
        form = PointForm()
        area = Area.objects.get(pk=id)
        points = Point.objects.filter(area=area.id)
        location = []
        for p in points:
            coordinate = (p.latitude, p.longitude)
            location.append(coordinate)
        print(location)      
           
        print(len(location))
        if len(location)!=0:
            map_location = location[0] # First Point
            show_map(map_location)   
            my_map = draw_area(location, area.color, area.fill_color, area.name) 
            m = my_map._repr_html_()        
        else:
            map_location = [28.5665, 77.103104]
            my_map = show_map(map_location) 
            m = my_map._repr_html_()      
       
        context:dict = {
            'form':form,
            'points': points,
            'area':area,
            'map':m
            }
    else:
        form = PointForm(request.POST)
        if form.is_valid:
           point =  form.save()  
           area = Area.objects.get(pk=point.area.id)
           points = Point.objects.filter(area=area.id)
           form = PointForm()
           context = {
               'points': points,
               'area':area,
               'form':form
           }
    return render(request,'noc/point_plot.html', context)

def mark_obstruction(request):
    return render(request, 'noc/template.html')


def delete_point(request, point_id):

    point = Point.objects.get(pk=point_id)
    area = point.area
    point.delete()
    return redirect('point_plot',id=area.id)

def area_list(request):
    area_list = Area.objects.all()
    for area in area_list:
        points = Point.objects.filter(id=area.id)
    context:dict = {
        'area_list': area_list,
        'points': points
    }

    return render(request, 'noc/area_list.html', context)


def delete_area(request, id):
    area = Area.objects.get(pk=id)    
    area.delete()
    return redirect('area_list')

def edit_area(request, id):
    if request.method == "GET":
        point = Point.objects.filter(pk=id)
    return redirect('point_plot', id=id)