from django.urls import path
from user.views import login,logout,register
urlpatterns=[
    path('login',login,name='login'),
    path('register',register,name='register'),
    path('logout',logout,name='logout')
]