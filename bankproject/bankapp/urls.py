from django.urls import path
from bankapp import views
app_name='bankapp'

urlpatterns = [
    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form/',views.form,name='form'),
    path('form/logout/',views.logout,name='logout'),

    path('form/newpage/',views.newpage,name='newpage'),
    path('form/newpage/index', views.msg, name='msg'),

]