import logging
from django.core.mail import send_mail
from rest_framework.response import Response


logger = logging.getLogger(__name__)


class APIMixin(object):
    def success(self, data=None, status=None):
        if data is None:
            return Response(data={
                'status': 'OK',
            }, status=status)
        return Response(data={
            'status': 'OK',
            'data': data
        }, status=status)

    def fail(self, errors):
        return Response(data={
            'status': 'FAIL',
            'errors': errors,
        }, status=400)


class SendMailMixin(object):
    _from_email = 'admin_order@gmail.com'

    def send_mail(self, data):
        try:
            message = self.generate_mail_message(data)
            # this solution acceptable for `console.EmailBacken` only
            # in another case (f.ex. `smtp.EmailBackend`) should be used some waiting task (f.ex. via Celery)
            send_mail(
                subject=data['order_by_name'],
                message=message,
                from_email=self._from_email,
                recipient_list=[data['order_by_email']]
            )
        except Exception as ex:
            logger.exception(ex, exc_info=True)

    @staticmethod
    def generate_mail_message(data):
        return f"Hi {data['order_by_name']}, your table order confirmed.\nDetails:\n"\
               f"Table number: {data['table']}\nDate: {data['order_date']}"
