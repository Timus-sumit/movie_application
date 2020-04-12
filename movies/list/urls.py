from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
     path ('content/',views.create, name='create'),
         path('lists/', views.ListList.as_view(),name='list-list'),
    path('lists/<int:pk>/', views.ListDetail.as_view(),name='list-detail'),
    path('users/', views.UserList.as_view(),name='user-list'),
path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
path('', views.api_root),
path('lists/<int:pk>/highlight/', views.ListHighlight.as_view(),name='list-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
