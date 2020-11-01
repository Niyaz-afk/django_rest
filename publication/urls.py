from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'posts'
urlpatterns = [

    path('post', views.PostView.as_view()),
    path('post/<int:pk>/', views.PostView.as_view())


]



#urlpatterns = format_suffix_patterns(urlpatterns)
