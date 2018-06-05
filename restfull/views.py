from django.shortcuts import render

# Create your views here.


from restfull.models import music,travel
from restfull.serializers import MusciSerializer,TravelSerializer

from rest_framework import viewsets

class MusicViewSet(viewsets.ModelViewSet):
    queryset = music.objects.all()
    serializer_class = MusciSerializer

class TravelViewSet(viewsets.ModelViewSet):
    queryset = travel.objects.all()
    serializer_class = TravelSerializer

# from django.template import loader
#
# from django.http import HttpResponse
#
# def index(request):
#     template = loader.get_template('demo/index.html')
#     return HttpResponse(template.render())