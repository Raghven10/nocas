from collections import namedtuple
import numpy as np


def get_angle(p1, p2):

    '''
    This function Returns angle value in degree from the location p1 to location p2

    Parameters it accepts :
    p1 : namedtuple with lat lon
    p2 : namedtuple with lat lon

    This function Return the vlaue of degree in the data type float

    Pleae also refers to for better understanding : https://gist.github.com/jeromer/2005586
    '''

    longitude_diff = np.radians(p2.lon - p1.lon)

    latitude1 = np.radians(p1.lat)
    latitude2 = np.radians(p2.lat)

    x_vector = np.sin(longitude_diff) * np.cos(latitude2)
    y_vector = (np.cos(latitude1) * np.sin(latitude2)
        - (np.sin(latitude1) * np.cos(latitude2)
        * np.cos(longitude_diff)))
    angle = np.degrees(np.arctan2(x_vector, y_vector))

    # Checking and adjustring angle value on the scale of 360
    if angle < 0:
        return angle + 360
    return angle

def find_angle(locations):

    '''
    This function Returns angle value in degree from the location p1 to location p2

    Parameters it accepts :
    p1 : namedtuple with lat lon
    p2 : namedtuple with lat lon

    This function Return the vlaue of degree in the data type float

    Pleae also refers to for better understanding : https://gist.github.com/jeromer/2005586
    '''
    Point = namedtuple('Point', field_names=['lat', 'lon'])

    # creating point from Point named tuple
    p1 = Point(locations[0][0], locations[0][1])
    p2 = Point(locations[1][0], locations[1][1])

    longitude_diff = np.radians(p2.lon - p1.lon)

    latitude1 = np.radians(p1.lat)
    latitude2 = np.radians(p2.lat)

    x_vector = np.sin(longitude_diff) * np.cos(latitude2)
    y_vector = (np.cos(latitude1) * np.sin(latitude2)
        - (np.sin(latitude1) * np.cos(latitude2)
        * np.cos(longitude_diff)))
    angle = np.degrees(np.arctan2(x_vector, y_vector))

    # Checking and adjustring angle value on the scale of 360
    if angle < 0:
        return angle + 360
    return angle