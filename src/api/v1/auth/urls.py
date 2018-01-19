from django.urls import include, path

from rest_framework import routers
from src.api.v1.auth import views


router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('tokens', views.TokenViewSet)

urlpatterns = [
    path('signup/', views.OTPRegisterView.as_view(), name="signup"),
    path('signin/', views.OTPLoginView.as_view(), name="signin"),
    path('captcha/', views.OTPCaptchaView.as_view(), name="captcha"),
] + router.urls
