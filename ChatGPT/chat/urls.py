from django.urls import path
from .views import render_index
from .views import HotelNameView

urlpatterns = [
    path('', render_index, name='index'),
    path('hotelName/', HotelNameView.as_view(), name='hotel_name'),
]