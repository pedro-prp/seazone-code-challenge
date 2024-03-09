from django.urls import path
from .views import AdvertisementListCreateView, AdvertisementDetailView

urlpatterns = [
    path("", AdvertisementListCreateView.as_view(), name="advertisement-list-create"),
    path("<str:pk>/", AdvertisementDetailView.as_view(), name="advertisement-detail"),
]
