#from django.contrib import admin
from django.urls import path
from . import views  #dot is this directory


urlpatterns = [
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
    path('babe/', views.babe , name='babe'),

    #path('admin/', admin.site.urls),
    # you can change admin path like 'good/'
]
