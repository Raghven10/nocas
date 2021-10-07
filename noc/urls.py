from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

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

                  # ex: /airport_list
                  path('airport_list/', views.airport_list, name='airport_list'),

                  # ex: /airports/5/
                  path('airports/<int:airport_id>/', views.airport_details, name='airport_details'),

                    # ex: /delete/5/
                  path('delete/<int:id>/', views.delete_airport, name='delete_airport'),



              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
