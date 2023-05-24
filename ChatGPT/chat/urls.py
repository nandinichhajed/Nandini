from django.urls import path
from .views import *

urlpatterns = [
    path('', render_index, name='index'),
    path('hotelName/', HotelNameView.as_view(), name='hotel_name'),
    path('process/', ProcessView.as_view(), name='process'),
    path('process/prompt', PromptView.as_view(), name='prompt'),
    
]