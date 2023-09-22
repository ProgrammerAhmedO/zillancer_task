from django.urls import path
from BaseApp import views
from .views import (
    CRMLedListCreateView,
    CRMLedRetrieveUpdateDestroyView,
    MASSlmListCreateView,
    MASSlmRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('crmleds/', CRMLedListCreateView.as_view(), name='crmled-list-create'),
    path('crmleds/<int:pk>/', CRMLedRetrieveUpdateDestroyView.as_view(), name='crmled-detail'),
    path('masslms/', MASSlmListCreateView.as_view(), name='masslm-list-create'),
    path('masslms/<int:pk>/', MASSlmRetrieveUpdateDestroyView.as_view(), name='masslm-detail'),
    path('forecast/', views.forecast_view, name='forecast_view'),
]