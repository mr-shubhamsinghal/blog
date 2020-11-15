from django.urls import path

from bloggingapp.views import blog_view


app_name = 'blog_app'

urlpatterns = [
    	path('', blog_view, name='blog_view'),
    ]
