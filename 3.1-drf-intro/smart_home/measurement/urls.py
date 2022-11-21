from django.urls import path

from measurement.views import ADD_Mesuarment, SensorView, SensorsView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', ADD_Mesuarment.as_view()),
    


    # TODO: зарегистрируйте необходимые маршруты
]
