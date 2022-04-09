"""BookFace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view()),
    path('home/', views.Base.as_view(), name="base"),
    path('register/', views.AddUserView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.log_out, name="logout"),
    path('edit/', views.edit_profile, name="edit"),
    path('add_post/', views.AddPost.as_view(), name="add_post"),
    path('user/<int:pk>/', views.ProfileView.as_view(), name="profile"),
    path('post/<int:pk>/', views.PostView.as_view(), name="post_view"),
    path('post/<int:pk>/comment/', views.MakeCommentBlog.as_view(), name="make_comment_blog"),
    path('user/<int:pk>/send_message/', views.SendMessage.as_view(), name="send_message"),
    path('messages/', views.ReadMessages.as_view(), name="read_messages"),
]
