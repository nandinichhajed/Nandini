from django.urls import path
from .views import HotelNameView

urlpatterns = [
    path('hotelName', HotelNameView.as_view(), name='hotelName'),
]