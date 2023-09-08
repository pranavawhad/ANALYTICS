from rest_framework import serializers
from .models import *

class Website(serializers.ModelSerializer):
    class Meta:
        model = WebInfo
        fields = '__all__'
   
class Info(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
        
class site(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'

class Web(serializers.ModelSerializer):
    class Meta:
        model = Hover
        fields = '__all__'
        