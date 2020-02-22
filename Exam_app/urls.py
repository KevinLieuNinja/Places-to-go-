from django.urls import path
from . import views

urlpatterns= [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('newTrip', views.newTrip),
    path('editTrip/<int:id>', views.editTrip),
    path('view/<int:id>', views.view),
    path('create_trip', views.create_trip),
    path('delete_trip/<int:id>',views.delete_trip),
    path('update_trip/<int:id>', views.update_trip),
]