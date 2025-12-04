
from . import views
from django.urls import path


urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloEthiopia.as_view()),
    path('reservation', views.home),    
]
