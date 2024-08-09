from django.http import JsonResponse
from django.shortcuts import render

#third party imports 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post

class TestView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self,request,*args,**kwargs):
        data ={
            'name':"amal",
            "age":23
        }
        qs=Post.objects.all()
        post= qs.first()  #instead of serializing a query set, we can serialize one instance and look at that
        # serializer=PostSerializer(qs,many=True)
        serializer=PostSerializer(post)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer= PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
