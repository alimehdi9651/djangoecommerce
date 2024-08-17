from django.urls import path

from main import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('c/login', views.login_view, name = 'login'),
    path('c/register', views.register_view, name = 'register'),
    path('c/dashboard', views.dashboard_view, name = 'dashboard'),
    path('s/login', views.slogin_view, name = 'seller_login'),
    path('s/register', views.sregister_view, name = 'seller_register'),
    path('s/dashboard', views.sdashboard_view, name = 'seller_dashboard'),
    path('logout', views.logout_view, name = 'logout'),   
]