"""
URL configuration for phonebook_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

'''
urlpatterns = [
    path('admin/', admin.site.urls),
]
'''
# contacts/urls.py
from django.urls import path
from contacts import views

# contacts/urls.py

urlpatterns = [
   
    path('', views.signup, name='signup'), 
    path('login/', views.log_in, name='login'),     
    path('logout/', views.logout_view, name='logout'),
   
    path('phonebooks/', views.phonebook_list, name='phonebook_list'),
    path('phonebooks/create/', views.phonebook_create, name='phonebook_create'),
    path('phonebooks/<int:pk>/', views.phonebook_detail, name='phonebook_detail'),
    path('phonebooks/<int:pk>/edit/', views.phonebook_edit, name='phonebook_edit'),
    path('phonebooks/<int:pk>/delete/', views.phonebook_delete, name='phonebook_delete'),

    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/create/', views.contact_create, name='contact_create'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contacts/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    path('phonebook-specific/<int:pk>/', views.phonebook_specific, name='phonebook_specific'),
    path('phonebook-contacts/', views.phonebook_contacts, name='phonebook_contacts'),

    path('dial-phonebook/',views.dial_phonebook,name='dial_phonebook'),

    path('call-records/',views.display_call_records,name='display_call_records'),
]

