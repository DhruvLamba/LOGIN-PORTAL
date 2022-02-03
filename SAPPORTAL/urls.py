from django.urls import path
from SAPPORTAL import views

urlpatterns = [
    path('', views.indexUser, name='home'),
    path('main', views.about, name='main'),
    path('logout', views.logoutuser, name='logout'),
]