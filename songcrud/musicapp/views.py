# from django.http import HttpResponse

# # Create your views here.

# def index(request):
#     return HttpResponse("Hello, Welcome to my Music App!!!, Do have a wonderful time!!!")


from rest_framework import generics

from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer   

class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer  