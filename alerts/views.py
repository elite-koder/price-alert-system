from rest_framework.viewsets import mixins, GenericViewSet
from alerts.serializers import AlertSerializer
from alerts.models import Alert
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend    


class AlertViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 2
    pagination_class.max_page_size = 10
    pagination_class.page_query_param = "offset"
    pagination_class.page_size_query_param = "page_size"
