# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorChangeSerializer, SensorSerializer



class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    def post(self,request):
        review = SensorSerializer(data = review.data)
        if review.is_valid:
            review.save
        return Response({'status':'ok'})


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class ADD_Mesuarment(CreateAPIView):
    queryset = Measurement.objects.all()
    erializer_class = MeasurementSerializer












