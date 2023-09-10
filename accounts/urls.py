from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('generate/', TokenObtainPairView.as_view(), name='token_generate'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("verify/", TokenVerifyView.as_view(), name="verify")

]