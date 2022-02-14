from django.urls import path
from .views import index, vote, result

urlpatterns = [
    path("", index, name="index"),
    path("vote/<int:pk>", vote, name="vote"),
    path("result/<int:pk>", result, name="result"),
]
