from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterView, UserView, LogoutView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('user', UserView.as_view(), name='user'),
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('test/', views.TestView.as_view(), name='test'),
    path('logout', LogoutView.as_view(), name='logout'),
]
