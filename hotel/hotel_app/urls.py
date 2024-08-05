from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('admin/', views.Admin, name="admin"),
    path('Register/', views.login_signup_view, name="register"),
    path('regular/',views.contact_view, name="contact"),
    path('contact-success/', views.contact_success_view, name='contact_success'),
]
