from collections import namedtuple
import numpy as np
import folium

from .angle import get_angle


def getArrows(locations, color='blue', size=6, n_arrows=1):

    '''
    Get a list of placed and rotated arrows or markers to be plotted

    Parameters
    locations : list of lists of latitude longitude that represent the begining and end of Line.
                    this function Return list of arrows or the markers
    '''

    Point = namedtuple('Point', field_names=['lat', 'lon'])

    # creating point from Point named tuple
    point1 = Point(locations[0][0], locations[0][1])
    point2 = Point(locations[1][0], locations[1][1])

    # calculate the rotation required for the marker.
    #Reducing 90 to account for the orientation of marker
    # Get the degree of rotation
    angle = get_angle(point1, point2) - 90

    # get the evenly space list of latitudes and longitudes for the required arrows

    arrow_latitude = np.linspace(point1.lat, point2.lat, n_arrows + 2)[1:n_arrows+1]
    arrow_longitude = np.linspace(point1.lon, point2.lon, n_arrows + 2)[1:n_arrows+1]

    final_arrows = []

    #creating each "arrow" and appending them to our arrows list
    for points in zip(arrow_latitude, arrow_longitude):
        final_arrows.append(folium.RegularPolygonMarker(location=points,
                      fill_color=color, number_of_sides=3,
                      radius=size, rotation=angle))
    return final_arrows