from django.contrib import admin
from django.urls import path,include
from namik import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inde,name='inde'),
    path('about/',views.about,name='about'),
    path('blogs/',views.blogs,name='blogs'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu,name='menu'),
    path('products/',views.products,name='products'),
    path('logout/', LogoutView.as_view(next_page='inde'), name='logout'),
    path('register/', views.register, name='register'),
]