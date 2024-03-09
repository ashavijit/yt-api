from rest_framework import serializers
from .models import *

class YtVideosSerializer(serializers.ModelSerializer):

    class Meta:
        model = YtVideos
        fields = '__all__'