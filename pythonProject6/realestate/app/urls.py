from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login', views.login,name='login'),
    path('signup', views.signup,name='signup'),
    path('aboutus', views.aboutus,name='aboutus'),
    path('services',views.services,name='services'),
    path('commercial',views.commercial,name='commercial'),
    path('Lands',views.Lands,name='Lands'),
    path('Residential',views.Residential,name='Residential'),
    path('Hyderabad',views.Hyderabad,name='Hyderabad'),
    path('Vijayawada',views.Vijayawada,name='Vijayawada'),
    path('transaction',views.transaction,name='transaction'),
    path('logout', views.logout,name='logout'),
    path('logouthome', views.logouthome,name='logouthome'),
    path('changepwd/',views.changepwd,name='changepwd'),
    path('changepwd1/',views.changepwd1,name='changepwd1')


]