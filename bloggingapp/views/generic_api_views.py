from rest_framework import generics

from bloggingapp.models import BlogModel
from bloggingapp.serializers import BlogSerializer


class BlogListCreateAPIView(generics.ListCreateAPIView):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer


class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
