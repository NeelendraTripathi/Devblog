from django.urls import path
from . import views


urlpatterns =[
    path('', views.post_list , name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    # The URL for the "Thank You" page after a successful submission
    path('contact/success/', views.contact_success, name='contact_success'),
    
]