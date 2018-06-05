from rest_framework import serializers
from restfull.models import  music,travel


class MusciSerializer(serializers.ModelSerializer):
    class Meta:
        model = music
        # fields = '_all_'
        fields = ('id','song','singer','last_modify_date','created')


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = travel
        fields = '_all_'