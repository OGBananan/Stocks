from django.urls import path
from common_utils import views

urlpatterns = [
    path('health/', views.health_check),
]
