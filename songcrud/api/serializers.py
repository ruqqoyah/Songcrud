from django.contrib.auth.models import Song
from rest_framework import serializers
#from datetime import datetime


#serializing models 

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = song
        fields = ['title', 'date_released']
