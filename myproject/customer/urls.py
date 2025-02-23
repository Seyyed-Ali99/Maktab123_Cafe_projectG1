from django.urls import path
from .views import (
    login_user_view,
    user_logout,
    profile,
    view_messages,
    send_message,
    home_view,
    about_view,
    register_user_view,

)

urlpatterns = [
    path('',home_view, name='home'),
    path('about/',about_view,name='about'),

    path('login/',login_user_view,name='login'),
    path('register/',register_user_view,name='register'),
    path('admin/logout/', user_logout, name='logout'),
    path('admin/profile/', profile, name='profile'),
    path('admin/messages/', send_message, name='send_message'),
     path('admin/view-messages/', view_messages, name='view_messages'),
]
