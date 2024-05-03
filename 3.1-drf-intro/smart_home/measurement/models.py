from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='Measurement')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)