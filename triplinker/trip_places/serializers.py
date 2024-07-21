from rest_framework import serializers

from .models import Place


class TripPlaceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        exclude = ['place_pic', 'who_added_place_on_site', 'timestamp',
                   'followers']
