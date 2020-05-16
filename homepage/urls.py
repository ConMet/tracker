from django.urls import include, path
from homepage import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]
