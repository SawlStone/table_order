import pytest

from api.serializers import TableOrderCreateSerializer


@pytest.fixture()
def order():
    return {
        "table": "1",
        "order_date": "2020-05-07",
        "order_by_name": "John",
        "order_by_email": "john@gmail.com",
        "additional_info": "Some info",
    }


@pytest.mark.django_db
class TestTableOrderCreateSerializer:

    def test_fields(self, order):
        serializer = TableOrderCreateSerializer(data=order)
        serializer.is_valid()
        assert order == serializer.data

