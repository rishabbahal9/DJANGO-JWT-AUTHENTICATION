from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterView, UserView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('user', UserView.as_view()),
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('test/', views.TestView.as_view(), name='test'),
]
