
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

