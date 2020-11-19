
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from bloggingapp.models import BlogModel
from bloggingapp.serializers import BlogSerializer


class BlogViewSets(viewsets.ViewSet):
	def list(self, request):
		queryset = BlogModel.objects.all()
		serializer = BlogSerializer(queryset, many=True)
		return Response(serializer.data)


	# Return one blog item
	def retrieve(self, request, pk=None):
		queryset = BlogModel.objects.all()
		if pk is not None:
			blog = get_object_or_404(queryset, pk=pk)
			serializer = BlogSerializer(blog)
			return Response(serializer.data)
