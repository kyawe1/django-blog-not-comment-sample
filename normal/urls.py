from django.urls import path
import normal.views as view
urlpatterns=[
    path('',view.home,name='home'),
    path('about',view.about,name='about'),
    path('contact',view.contact,name='contact')
]