from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('authenticator.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name="login"),
    path('logout/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name="logout"),
]