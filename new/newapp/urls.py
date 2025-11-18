from django.urls import path
from . import views

urlpatterns = [    
    path("newapp/create_menu/", views.create_menu, name="create_menu"),
    path("newapp/list_menu/", views.list_menu, name="list_menu"),
    path("newapp/menu/<int:pk>/", views.menu_details, name="menu_details"),
    path("newapp/delete_menu/<int:pk>/", views.delete_item, name="delete_menu")
]
