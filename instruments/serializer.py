from rest_framework import serializers
from .models import Instrument

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields =['id','store_name', 'instrument', 'model' , 'price' , 'desc']