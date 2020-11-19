from django.urls import path

from bloggingapp.views import (blog_view, BlogAPIView, BlogViewSets,
							   BlogListCreateAPIView,
							   BlogRetrieveUpdateDestroyAPIView)


app_name = 'blog_app'


blog_list = BlogViewSets.as_view({
		'get': 'list',
	})

blog_detail = BlogViewSets.as_view({
		'get': 'retrieve',
	})


urlpatterns = [
    	path('fbv/', blog_view, name='blog_view'),

    	path('cbv_apiview/', BlogAPIView.as_view(), name='blog_api_view'),

    	path('cbv_generic_lc_view/', BlogListCreateAPIView.as_view(),
    		 name='blog_generic_lc_view'),

    	path('cbv_generic_rud_view/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(),
    		 name='blog_generic_rud_view'),

    	path('cbv_viewsets_list_view/', blog_list, name='blog_viewsets_list'),

    	path('cbv_viewsets_detail_view/<int:pk>/', blog_detail, name='blog_viewsets_detail'),
    ]
