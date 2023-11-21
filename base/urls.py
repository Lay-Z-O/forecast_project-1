from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('base/', views.base, name="base"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('overview/', views.overview, name="overview"),
    path('forecast/', views.forecast, name="forecast"),
    path('information/', views.information, name="info"),
    path('profile/', views.profile, name="profile"),
]