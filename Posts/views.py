from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Posts
from .serializers import PostsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication


# Create your views here.

class PostCreateView(ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all() 
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @csrf_exempt
    @api_view(['post'])
    def post(self, request):
        serializer = PostsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(photo = request.data.get('post_image'))
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostViewSet(ModelViewSet):
    queryset = Posts.objects.none()
    serializer_class = PostsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', ]

    def list(self, request):
        query_set = Posts.objects.all()
        return Response(self.serializer_class(query_set, many=True).data,
                        status=status.HTTP_200_OK)
    
    


