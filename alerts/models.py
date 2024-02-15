from django.db import models

# Create your models here.


class AlertStatus(models.TextChoices):
    CREATED = "CREATED"
    TRIGGERED = "TRIGGERED"
    DELETED = "DELETED"
    IN_QUEUE = "IN_QUEUE"


class Alert(models.Model):
    scrip = models.ForeignKey("scrips.Scrip", on_delete=models.CASCADE)
    target_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=25, choices=AlertStatus.choices, default=AlertStatus.CREATED)
    high_target_price = models.BooleanField(default=True)
