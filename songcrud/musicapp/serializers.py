from .models import Artiste, Song
from rest_framework import serializers
#from datetime import datetime


#serializing models 
class ArtisteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artiste
        fields=(
        "id",
        "first_name",
         "last_name",
         "Age",
        )

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields=(
        "id",
        "title",
         "date_released",
        )
