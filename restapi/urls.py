from django.urls import path
from .views import PostsAPIView, postDetailsAPIView

urlpatterns = [
    path('api/', PostsAPIView.as_view()),
    path('api/<int:pk>', postDetailsAPIView.as_view()),
]