from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Instrument
from .serializer import InstrumentSerializer
from .permissions import IsOwnerReadAndPost

class InstrumentListView(ListCreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [IsAuthenticated]

class InstrumentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [IsAuthenticated, IsOwnerReadAndPost]