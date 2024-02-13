from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.Serializer):
	title = serializers.CharField(label= 'Enter Title' )
	content = serializers.CharField( label = 'Description')
	owner = serializers.CharField( label = 'Owner')
	Headquarters = serializers.CharField(label= 'Headquarters' )
	founded = serializers.IntegerField( label = 'Founded')
        