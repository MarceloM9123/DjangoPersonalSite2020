from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('blog/', views.blog),
    path('shop/', views.products),
]
