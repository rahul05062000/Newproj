# serializers.py
from rest_framework import serializers
from .models import  WatchList, Streamplatform
from django.utils import timezone



class StreamplatformSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    about = serializers.CharField(max_length=50)
    website = serializers.URLField(max_length=200)

    def create(self, validated_data):
        """create and return a new `streampltform` instance, given the validated data """
        return Streamplatform.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        update the instance of `straampltform`
        """
        instance.name=validated_data.get('name',instance.name)
        instance.about=validated_data.get('about',instance.about)
        instance.website=validated_data.get('website',instance.website)
        instance.save()
        return instance

    
class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    stroyline = serializers.CharField(max_length=200)
    # platform=models.ForeignKey(Streamplatform,on_delete=models.CASCADE)
    active=serializers.BooleanField(default=True)
    created = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        """
        Create and return a new `WatchList` instance, given the validated data.
        """
        return WatchList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `WatchList` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.stroyline = validated_data.get('stroyline', instance.stroyline)
        instance.active = validated_data.get('active', instance.active)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
