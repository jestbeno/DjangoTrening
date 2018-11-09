from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('calendar', views.calendar, name = 'calendar'),
    path('login', auth_views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', auth_views.logout, {'next_page':'/'}, name = 'logout'),
    path('entry/<int:pk>', views.details, name = 'details'),
    path('entry/add', views.add, name = 'add'),
    path('entry/delete/<int:pk>', views.delete, name = 'delete'),


]
