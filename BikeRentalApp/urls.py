
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('payment/', views.payment, name='payment'),
    path('about/',views.about,name="about"),
    path('contact/', views.contact, name="contact"),
    path('Bikes/', views.Bikes, name="Bikes"),

]
