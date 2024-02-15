from alerts.models import Alert, AlertStatus
from django.db import transaction
from alerts.tasks import trigger_email

def post_price_change_handler(scrip):
    with transaction.atomic():
        alert_ids = []
        high_alerts = Alert.objects.filter(scrip=scrip, target_price__gte=scrip.price, status=AlertStatus.CREATED, high_target_price=True)
        alert_ids.extend(high_alerts.values_list('id', flat=True))
        low_alerts = Alert.objects.filter(scrip=scrip, target_price__lte=scrip.price, status=AlertStatus.CREATED, high_target_price=False)
        alert_ids.extend(low_alerts.values_list('id', flat=True))
        Alert.objects.filter(id__in=alert_ids).update(status=AlertStatus.IN_QUEUE)
        print("alert_ids", alert_ids)
        for alert_id in alert_ids:
            print("calling celery", alert_id)
            trigger_email.delay(alert_id)

        