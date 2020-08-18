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
    # actions = serializers.RelatedField(many=True, read_only=True)
    #actions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    actions = EventActionSerializer(many=True)

    class Meta:
        model = Event
        #fields = ('id', 'title', 'short_desc', 'confirmed_date', 'category', 'muni', 'actions')
        fields = '__all__'