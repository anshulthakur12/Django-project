from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other_page, name='other'),
    path('form_page/', views.form_name_view, name='form_page'),
    path('registration/', views.registration_page, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special')
 ]