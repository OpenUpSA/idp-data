from rest_framework import serializers
from .models import Event, Category, Municipality, EventAction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'

class EventActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAction
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    muni = MunicipalitySerializer()
    actions = EventActionSerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'