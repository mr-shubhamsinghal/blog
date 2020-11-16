from django.urls import path

from bloggingapp.views import blog_view, BlogAPIView, BlogListCreateAPIView, BlogRetrieveUpdateDestroyAPIView


app_name = 'blog_app'

urlpatterns = [
    	path('fbv/', blog_view, name='blog_view'),
    	path('cbv_apiview/', BlogAPIView.as_view(), name='blog_api_view'),
    	path('cbv_generic_lc_view/', BlogListCreateAPIView.as_view(), name='blog_generic_lc_view'),
    	path('cbv_generic_rud_view/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog_generic_rud_view'),
    ]
