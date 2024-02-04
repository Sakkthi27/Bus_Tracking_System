from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.index ,name="index" ),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    path('routes',views.routes,name="bus_routes"),
    path('trip_planner',views.trip_planner,name="trip_planner"),
    path('stops',views.stops,name="stops"),
    path('favourites',views.favourites,name="favourites"),
    path('faq',views.faq,name="faq"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
]