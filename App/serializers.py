from rest_framework.serializers import ModelSerializer 
from .models import Books
from rest_framework import serializers


class BooksSerializer(ModelSerializer):
    class Meta :
        model = Books 
        fields = '__all__'
        
        
class ModifyVideoSerializer(serializers.Serializer):
    youtube_link = serializers.URLField()
    text_to_add = serializers.CharField(default='add text', required=False)