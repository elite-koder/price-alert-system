from celery import shared_task
from alerts.models import Alert, AlertStatus

@shared_task
def trigger_email(alert_id):
    print('celery task')
    alert = Alert.objects.get(id=alert_id)
    alert.status = AlertStatus.TRIGGERED
    alert.save()
    print(f"alert id {alert_id}, target price reached {alert.target_price}")