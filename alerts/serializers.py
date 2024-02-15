from rest_framework.serializers import ModelSerializer
from alerts.models import Alert

class AlertSerializer(ModelSerializer):
    class Meta:
        model = Alert
        exclude = ['high_target_price']

    def create(self, validated_data):
        validated_data["high_target_price"] = validated_data["target_price"] > validated_data['scrip'].price
        return super().create(validated_data)
        
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)