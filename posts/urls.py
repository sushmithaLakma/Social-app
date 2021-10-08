from django.urls import path
from .views import (
	home_view, 
	post_view_json, 
	PostDeleteView, 
	PostCreateView,
)

app_name = 'posts'

urlpatterns = [
	path('', home_view, name='home-view'),
	path('<int:pk>/delete/',
	     PostDeleteView.as_view(), name='post_delete'),
	path('new/', PostCreateView.as_view(), name='post_new'),

	# json # endpoints
	path('posts-json/', post_view_json, name='posts-view-json'),
]