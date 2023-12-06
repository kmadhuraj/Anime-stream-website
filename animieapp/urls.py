from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name="index"),
    path ('signup',views.Signup,name="signup"),
    
    # path ('signup',views.Signup,name="signup"),
    
    path ('login',views.handlelogin,name="login"),
    path('logout',views.handlelogout,name='logout'),
    path ('header',views.header,name="header"),
    path('contact',views.contact,name="contact"),
    path('mylist',views.mylist,name="mylist"),
    path('watch/<int:watch_id>/',views.watchv,name="watch"),
]