from django.urls import path

from bloggingapp.views import blog_view, BlogAPIView


app_name = 'blog_app'

urlpatterns = [
    	path('fbv/', blog_view, name='blog_view'),
    	path('cbv_apiview/', BlogAPIView.as_view(), name='blog_api_view'),
    ]
