# pyrefly: ignore [missing-import]
from . import views
from django.urls import path

urlpatterns=[
    path('users/',views.user_list),
    path('users/<int:pk>/',views.user_detail)
]
