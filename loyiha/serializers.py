from rest_framework import serializers
from .models import *


class LoyihaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Loyiha
        fields = '__all__'

class TalabalarSerializer(serializers.ModelSerializer):
    loyihalar = LoyihaSerializer(read_only=True, many=True)
    class Meta():
        model = Talabalar
        fields = '__all__'

class Eng_yaxshiSerializer(serializers.ModelSerializer):
    class Meta():

        model = Eng_yaxshi   
        fields = '__all__'     


