from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    
    path('', views.login_user, name="login_user"),
    path('question', views.question, name="question"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
    path('update_password', views.update_password, name="update_password"),
    path('search_question', views.search_question, name="search_question"),
]