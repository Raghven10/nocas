import io
from django.http import FileResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
import folium
from .models import Airport, Area, Point

# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from PIL import Image

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None


def printMyFile(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='filename.pdf')

def printFile(request, airport_id):
    airport = Airport.objects.get(pk=airport_id)
    airport_location = [airport.latitude_deg, airport.longitude_deg]
    my_map = folium.Map(location=airport_location, control_scale=True)
    ihs = folium.vector_layers.Circle(location=airport_location, fill="red", radius=20000, color="red", opacity=0.4,
                                              popup="IHS", tooltip="20 KM RED ZONE")
    ohs = folium.vector_layers.Circle(location=airport_location, fill="yellow", radius=60000, color="yellow",
                                              opacity=0.4)
    ihs.add_to(my_map)
    ohs.add_to(my_map)
    folium.Marker(location=airport_location,
                          popup='ARP %s Elevation: %d Feet' % (airport_location, airport.elevation_ft),
                          tooltip='ARP %s Elevation: %d Feet' % (airport_location, airport.elevation_ft)).add_to(my_map)
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
                folium.Marker([p.latitude, p.longitude],icon=div).add_to(my_map)                        
                coordinates.append(coordinate)
            shapesLayer = folium.FeatureGroup(name=area.name).add_to(my_map)    
            folium.Polygon(locations=coordinates, color=area.color, fill_color  = area.fill_color, tooltip=area.name).add_to(shapesLayer)
    folium.LayerControl().add_to(my_map)  
    my_map.fit_bounds(my_map.get_bounds())
    html = my_map.save('simple_dot_plot.html')
    
    return render(request, html)
    # template_src = my_map   
   
    # # buffer = io.BytesIO()
    # # p = canvas.Canvas(buffer)
    # # p.drawImage(m, 0, 0, 400, 400)
    # # p.showPage()
    # # p.save()
    # # buffer.seek(0)
    # # return FileResponse(buffer, as_attachment=True, filename='filename.pdf')
    # context_dict={}
    # template = get_template(template_src)
    # html  = template.render(context_dict)
    # result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    # if not pdf.err:
    #     return HttpResponse(result.getvalue(), content_type='application/pdf')
    # return None
    
