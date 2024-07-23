from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.TestHealth.as_view(), name='health_check')
]

from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.TestHealth.as_view(), name='health_check')
]
