from rest_framework.viewsets import mixins, GenericViewSet
from scrips.serializers import ScripSerializer
from scrips.models import Scrip

class ScripViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = ScripSerializer
    queryset = Scrip.objects.all()
