import folium
from .models import Airport, Area, Point

def show_map(location):
    my_map = folium.Map(location, control_scale=True, zoom_start=10, crs='EPSG3857', zoom_control=True, png_enabled=True, width='100%', height='100%')
    for airport in Airport.objects.all():
        airport_location = [airport.latitude_deg, airport.longitude_deg]
        ihs = folium.vector_layers.Circle(airport_location, fill="red", radius=5000, color="red", opacity=0.4,
                                              popup="5KM Radius", tooltip="5KM Radius")
        ihs.add_to(my_map)
        folium.Marker(airport_location,
                        popup='%s %s ARP %s ' % (airport.name, airport.ident, airport_location),
                        tooltip='%s ' % (airport.name)).add_to(my_map)
        
    return my_map
    

def draw_area(location,  color, fill_color, area_name):
    my_map = show_map(location[0])
     # create a layer on the map object
    shapesLayer = folium.FeatureGroup(name=area_name).add_to(my_map)    
    # create a polygon with the coordinates
    folium.Polygon(location, color=color,
                    fill_color=fill_color,tooltip=area_name,popup=location,
                    weight=2).add_to(shapesLayer)
    
    folium.LayerControl().add_to(my_map)  
    return my_map


def draw_route(location,  color, route_name):
    my_map = show_map(location[0])
     # create a layer on the map object
    shapesLayer = folium.FeatureGroup(name=route_name).add_to(my_map)    
    # create a polyline with the coordinates
    folium.PolyLine(location, color=color,
                    tooltip=route_name).add_to(shapesLayer)
    
    folium.LayerControl().add_to(my_map)  
    return my_map