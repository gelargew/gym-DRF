from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.snippet_list.as_view()),
    path('<int:pk>/', views.snippet_detail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)