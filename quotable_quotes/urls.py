from django.urls import path
from quotables_app import views

urlpatterns = [
    path('',views.main_page),
    path('register',views.register),
    path('login',views.login),
    path('quotes',views.quotes),
    path('quotes/<x>',views.edit_quote),
    path('users/<x>',views.show_user),
    path('add_quote',views.add_quote),
    path('logout',views.logout),
    path('delete/<x>',views.delete_this),
    path('update/<x>',views.update),
    path('add_favorite/<x>',views.add_favorite),
    path('remove_favorite/<x>',views.remove_favorite)
]
