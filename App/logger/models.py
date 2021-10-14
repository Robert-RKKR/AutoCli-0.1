from django.db import models

# Loggers models:
class LoggerData(models.Model):
    SEVERITY = (
        (1, 'DEBUG'),
        (2, 'INFO'),
        (3, 'WARNING'),
        (4, 'ERROR'),
        (5, 'CRITICAL'),
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    process = models.IntegerField()
    application = models.CharField(max_length=128)
    module = models.CharField(max_length=128, null=True)
    severity = models.IntegerField(choices=SEVERITY)
    message = models.CharField(max_length=1024)


class AdditionalData(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    logger = models.ForeignKey(LoggerData, on_delete=models.CASCADE)