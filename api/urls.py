from django.urls import path
from .views import SubarregloView

urlpatterns = [
    path('subarray/', SubarregloView.as_view(), name='subarray'),
]