from django.urls import path
from .views import InstrumentListView, InstrumentDetailView

urlpatterns = [
   
    path('', InstrumentListView.as_view(), name= 'instruments'),
    path('<int:pk>/',InstrumentDetailView.as_view(), name= 'instrument_detail'),

]