from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

app_name = "system"

urlpatterns = [
    path("", AllFundraisingView.as_view()),
    path("<int:pk>", FundraisingDetailView.as_view()),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh")
]
