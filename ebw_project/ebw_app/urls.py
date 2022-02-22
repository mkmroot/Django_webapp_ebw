from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="Home_Page" ),
    path('signup', views.signup, name="Registration_Page"),
    path('signin', views.signin, name="Registration_Page"),
    path('signout', views.signout, name="Registration_Page")
]
