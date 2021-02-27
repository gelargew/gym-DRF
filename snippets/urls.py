from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.snippet_list.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('<int:pk>/', views.snippet_detail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)