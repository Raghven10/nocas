from django.http import HttpResponse, Http404
from django.shortcuts import render
import pandas as pd
import folium
import csv

# Create your views here.
from django.template import loader

def index(request):
    return render(request, 'noc/index.html')



