from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializer import BlogPostSerializer
# Create your views here.
class BlogApiView(APIView):
    serializer_class = BlogPostSerializer
    def get(self,request):
        allposts = BlogPost.objects.all().values()
        return Response({'Message':'All Posts', 'POST_List' :allposts})
    
    def post(self,request):
        #print()
        serializer_obj = BlogPostSerializer(data = request.data)
        if (serializer_obj.is_valid()):
            BlogPost.objects.create(title = serializer_obj.data.get('title'),
                                    content = serializer_obj.data.get('content'),
                                    owner = serializer_obj.data.get('owner'),
                                    Headquarters = serializer_obj.data.get('Headquarters'),
                                    Founded  = serializer_obj.data.get('Founded')
                                    )
        Posts = BlogPost.objects.all().values()
        return Response({'Message':'New_Post_Added', 'New_Post' : Posts},status=200)
    