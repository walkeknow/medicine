from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from users.views import  user_login, user_logout

urlpatterns = [
    path('', include('authenticator.urls')),
    path('admin/', admin.site.urls),
    # path('login/', auth_views.LoginView.as_view(
    #     template_name='users/login.html'
    # ), name="login"),
    # path('logout/', auth_views.LoginView.as_view(
    #     template_name='users/login.html'
    # ), name="logout"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout")
]