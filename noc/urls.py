from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from noc import print_file

from . import views

urlpatterns = [
                  path('', views.airports, name='airports'),

                  # ex: /airports/
                  path('airports/', views.airports, name='airports'),

                  # ex: /airports/add/
                  path('airports/add/', views.add_airport, name='add_airport'),

                    # ex: /airports/add/
                  path('airports/add/<int:id>', views.add_airport, name='edit_airport'),

                  # ex: /mark_obstruction/
                  path('mark_obstruction/', views.mark_obstruction, name='mark_obstruction'),

                  # ex: /plot_route/
                  path('plot_route/', views.plot_route, name='plot_route'),

                  # ex: /area_plot/
                  path('area_plot/', views.area_plot, name='area_plot'),

                  # ex: /point_plot/
                  path('point_plot/<int:id>', views.point_plot, name='point_plot'),

                  # ex: /airport_list
                  path('airport_list/', views.airport_list, name='airport_list'),

                  # ex: /airports/5/
                  path('airports/<int:airport_id>/', views.airport_details, name='airport_details'),

                    # ex: /delete/5/
                  path('delete/<int:id>/', views.delete_airport, name='delete_airport'),

                  # ex: /airport_list
                  path('area_list/', views.area_list, name='area_list'),

                  # ex: /area_type
                  path('area_type/', views.area_type, name='area_type'),

                    # ex: /edit_area/5/
                  path('edit_area/<int:id>/', views.edit_area, name='edit_area'),

                    # ex: /delete_area/5/
                  path('delete_area/<int:id>/', views.delete_area, name='delete_area'),

                    # ex: /delete_area_type/5/
                  path('delete_area_type/<int:id>/', views.delete_area_type, name='delete_area_type'),
                   
                  path('route_plot/', views.route_plot, name='route_plot'),

                  path('waypoint_plot/<int:id>', views.waypoint_plot, name='waypoint_plot'),

                  path('delete_waypoint/<int:id>', views.delete_waypoint, name='delete_waypoint'),

                  # ex: /route_list
                  path('route_list/', views.route_list, name='route_list'),
                   
                  path('route_delete/<int:id>/', views.route_delete, name='route_delete'),

                    # ex: /delete_point/5/
                  path('delete_point/<int:point_id>/', views.delete_point, name='delete_point'),

                   # ex: /route_type
                  path('route_type/', views.route_type, name='route_type'),

                   # ex: /route_type
                  path('print_file/<int:airport_id>', print_file.printFile, name='print_file'),

                   # ex: /delete_route_type/5/
                  path('delete_route_type/<int:id>/', views.delete_route_type, name='delete_route_type'),



              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
