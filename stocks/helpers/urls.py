from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.TestHealth, name='health_check')
]
