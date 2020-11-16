
from rest_framework.views import APIView
from rest_framework.response import Response

from bloggingapp.models import BlogModel
from bloggingapp.serializers import BlogSerializer


class BlogAPIView(APIView):

	def get(self, request):
		blogs = BlogModel.objects.all()
		serializer = BlogSerializer(blogs, many=True)
		return Response({
				'success': True,
				'data': serializer.data
			})

	def post(self, request, *args, **kwargs):
		if request.data.get('title') != '':
			serializer = BlogSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response({
						'success': True,
						'message': 'APIView: post request fulfilled',
						'data': serializer.data
					})

	def put(self, request, *args, **kwargs):
		pk = request.data.get('id')
		if pk is not None:
			blog = BlogModel.objects.get(pk=int(pk))
			if blog:
				serializer = BlogSerializer(blog, data=request.data)
				if serializer.is_valid():
					serializer.save()
					return Response({
							'success': True,
							'message': 'APIView: updated blog post',
							'data': serializer.data
						})

	def delete(self, request, *args, **kwargs):
		pk = request.data.get('id')
		if pk is not None:
			blog = BlogModel.objects.get(pk=int(pk))
			if blog:
				blog.delete()
				return Response({
						'success': True,
						'message': 'APIView: delete request fulfilled',
					})

