from rest_framework import serializers

from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor','temperature','created_at']

class SensorSerializer(serializers.ModelSerializer):
    measurments = MeasurementSerializer(read_only=True, many=True)
    
    class Meta:
        model = Sensor
        fields = ['id','name','description','measurments']


