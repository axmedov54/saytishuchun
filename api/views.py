from django.shortcuts import render
from blog.models import Post
from .serializer import PostSerializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework import permissions
from .permissions import IsAuthorRead
from rest_framework.pagination import PageNumberPagination

class StandartPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5


class CRUDview(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostListViews(ListAPIView):
    permission_classes = (IsAuthorRead, )
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = StandartPagination


class PostCreateViuew(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers



class CreateViuew(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class ListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class DeleteViews(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
