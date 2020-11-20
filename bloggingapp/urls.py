from django.urls import path

from bloggingapp.views import (blog_view, BlogAPIView, BlogViewSets,
							   BlogListCreateAPIView, BlogModelViewSets,
							   BlogRetrieveUpdateDestroyAPIView)


app_name = 'blog_app'


blog_list = BlogViewSets.as_view({
		'get': 'list',
	})

blog_detail = BlogViewSets.as_view({
		'get': 'retrieve',
	})

blogmodel_list = BlogModelViewSets.as_view({
        'get': 'list',
    })

blogmodel_detail = BlogModelViewSets.as_view({
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

        path('cbv_viewsets_list/', blogmodel_list, name='blogmodel-list'),

        path('cbv_viewsets_detail/<int:pk>/', blogmodel_detail, name='blogmodel-detail'),
    ]
