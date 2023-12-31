
from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up,name='signup'),
    path('login/', views.user_login,name='login'),
    path('profile/', views.user_profile,name='profile'),
    path('logout/', views.user_logout,name='logout'),
    path('changepass/', views.user_change_pass,name='changepass'),
]
