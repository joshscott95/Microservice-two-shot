from django.urls import path
from .views import api_list_shoes, api_list_shoe

urlpatterns = [
    path('shoes/', api_list_shoes, name='api_list_shoes'),
    path('shoes/<int:pk>/', api_list_shoe, name='api_list_shoe'),
]
