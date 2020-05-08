import logging
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from .mixins import APIMixin, SendMailMixin
from .serializers import TableOrderCreateSerializer

logger = logging.getLogger(__name__)


class TableOrderCreateApiView(APIMixin, SendMailMixin, APIView):
    serializer_class = TableOrderCreateSerializer

    def post(self, request, *args, **kwargs):
        order = request.data.get('order')
        serializer = TableOrderCreateSerializer(data=order)

        if not serializer.is_valid():
            logger.error(f'Input data validation error. Details: {serializer.errors}')
            return self.fail(errors=serializer.errors)

        serializer.save()
        self.send_mail(data=serializer.data)
        logger.debug(f'Table order created. Details: {serializer.data}')

        return self.success(data=serializer.data, status=HTTP_201_CREATED)
