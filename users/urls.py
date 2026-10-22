from django.urls import path
from .views import RegisterView,LoginView,UserMeView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name='user-register'),
    path("login/", LoginView.as_view(), name="user-login"),
    path("me/", UserMeView.as_view(),name="me-user")
]
