from .views import RegisterAPI, Policy_page, policy_create_view
from knox import views as knox_views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', auth_views.LoginView.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('policy_detail.html/', Policy_page, name='My Policy'),
    path('create/', policy_create_view, name='policy-list')
    #path(r'custom/login/', CustomLoginView.as_view(), name='my_custom_login')

]
