from django.urls import path
from home import views
from django.conf.urls import url

urlpatterns = [path('add/', views.add), path('work/', views.work), path('progress/', views.progress), path('process', views.Process.as_view())]

