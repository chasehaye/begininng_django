from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finchs/', views.FinchList.as_view(), name='index'),
    path('finchs/<int:finch_id>/', views.finchs_detail, name='detail'),
    path('finchs/create', views.FinchCreate.as_view(), name='finchs_create'),
    path('finchs/<int:pk>/update/', views.FinchUpdate.as_view(), name='finchs_update'),
    path('finchs/<int:pk>/delete/', views.FinchDelete.as_view(), name='finchs_delete'),
    path('finchs/<int:finch_id>/add_location/', views.add_location, name='add_location'),
    path('finchs/<int:finch_id>/assoc_feed/<int:feed_id>/', views.assoc_feed, name='assoc_feed'),
    path('finchs/<int:finch_id>/unassoc_feed/<int:feed_id>/', views.unassoc_feed, name='unassoc_feed'),
    path('feeds/', views.FeedList.as_view(), name='feeds_index'),
    path('feeds/<int:pk>/', views.FeedDetail.as_view(), name='feeds_detail'),
    path('feeds/create/', views.FeedCreate.as_view(), name='feeds_create'),
    path('feeds/<int:pk>/update/', views.FeedUpdate.as_view(), name='feeds_update'),
    path('feeds/<int:pk>/delete/', views.FeedDelete.as_view(), name='feeds_delete'),
]
