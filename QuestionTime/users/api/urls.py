from django.urls import path
from users.api.views import CurrentUserAPIView

urlpatterns = [
    # provide username of user which is currently connected
    path('user/', CurrentUserAPIView.as_view(), name='current-user')
]