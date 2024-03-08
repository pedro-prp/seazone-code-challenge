from django.urls import path
from .views import BookingsListCreateView, BookingsDetailView

urlpatterns = [
    path("", BookingsListCreateView.as_view(), name="bookings-list-create"),
    path("<str:pk>/", BookingsDetailView.as_view(), name="bookings-detail"),
]
