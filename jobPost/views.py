from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from jobPost.models import Post
from jobPost.serializers import GetPostSerializer, MakePostSerializer


@api_view(['GET'])
def get_post(request):
    posts = Post.objects.all()
    serializer = GetPostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def make_post(request):
    serializer = MakePostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        return Response(status=HTTP_400_BAD_REQUEST)
