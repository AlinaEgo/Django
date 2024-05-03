from django.urls import path
from . import views

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', views.SensorsView.as_view(), name='sensors'),
    path('measurements/', views.MeasurementView.as_view(), name='measurements'),
    path('sensors/<pk>/', views.SensorView.as_view(), name='sensor_detail'),
]
