from django.urls import path
from . import views

app_name = 'hash_diary'
urlpatterns = [
	# ex: /diary/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /diary/packs/
	path('packs/', views.packs_list, name='packs_list'),
	# ex: /diary/packs/5/
	path('packs/<int:pk>/', views.PackDetail.as_view(), name='pack_detail'),
	# ex: /diary/trails/
	path('trails/', views.trails_list, name='trails_list'),
	# ex: diary/trails/121/
	path('trails/<int:pk>/', views.TrailDetail.as_view(), name='trail_detail'),
]