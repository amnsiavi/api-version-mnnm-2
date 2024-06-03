from rest_framework import serializers
from datetime import datetime
from watch_list.models import WatchList, StreamPlatform, Review



class ReviewSerialzer(serializers.ModelSerializer):
    
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    _watchlist = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        exclude = ['created','updated']
    
    def get__watchlist(self,object):
        return str(object.watchlist)
    def get_created_at(self,object):
        return object.created.strftime("%Y-%m-%d-%H:%M:%S")
    
    def get_updated_at(self,object):
        return object.updated.strftime("%Y-%m-%d-%H:%M:%S")
    
    def update(self,instance,validated_data):
        
        instance.rating = validated_data.get('rating',instance.rating)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.updated = datetime.now()
        instance.save()
        return instance





class WatchListSerializer(serializers.ModelSerializer):
    
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    _platform = serializers.SerializerMethodField()
    review = ReviewSerialzer(many=True,read_only=True)
    
    
    class Meta:
        model = WatchList
        exclude = ['created','updated']
    
    def get__platform(self,object):
        return str(object.platform)
    def get_created_at(self,object):
        return object.created.strftime("%Y-%m-%d %H:%M:%S")
    
    def get_updated_at(self,object):
        return object.updated.strftime("%Y-%m-%d %H:%M:%S")
    
    def update(self,instance,validated_data):
        
        instance.title = validated_data.get('title',instance.title)
        instance.storyline = validated_data.get('storyline',instance.storyline)
        instance.active = validated_data.get('active',instance.active)
        
        instance.updated = datetime.now()
        instance.save()
        return instance
        

class StreamPlatformSerialzer(serializers.ModelSerializer):
    
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    watch_list = WatchListSerializer(many=True,read_only=True)
    
    class Meta:
        model = StreamPlatform
        exclude = ['created','updated']
        
    
    def update(self, instance,validated_data):
        
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        
        instance.updated = datetime.now()
        instance.save()
        return instance
            
    def get_created_at(self,object):
        return object.created.strftime("%Y-%m-%d-%H:%M:%S")
    
    def get_updated_at(self,object):
        return object.updated.strftime("%Y-%m-%d-%H:%M:%S")
    



