from django.urls import path
from scrape import views

urlpatterns = [
    path('', views.scrape, name='scrape'),
    #path('', views.pulldata, name='pulldata'),
]
