from rest_framework.serializers import ModelSerializer
from scrips.models import Scrip
from alerts.handlers import post_price_change_handler

class ScripSerializer(ModelSerializer):
    class Meta:
        model = Scrip
        fields = ("id", "code", "price")

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        price_changed = "price" in validated_data and instance.price != validated_data["price"]
        print("price_changed", price_changed)
        ob = super().update(instance, validated_data)
        if price_changed:
            post_price_change_handler(ob)
        return ob