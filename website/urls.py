from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    
  #  path('on/',views.on ),
    path('of/',views.of )
]
