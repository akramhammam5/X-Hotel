from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name="Contact"),
    path('contact-success/', views.contact_success_view, name='contact_success'),
]