from django.urls import path
from .views import loginView,logoutView,registerView

urlpatterns = [

    path('login/', loginView, name='loginView'),
    path('logout/', logoutView, name='logoutView'),
    path('register/', registerView, name='registerView')
]
