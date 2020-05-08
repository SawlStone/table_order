Table ordering
=======================

Using Python 3.7

## Installation

$ cd table_order

$ pip install -r requirements.txt

$ python manage.py runserver

### Credentials

Admin user

login: admin

password: 12345

### API

#### Create table order:

##### Request

method: `POST`

endpoint: `api/table_order/create/`

params: 
```json
{
    "order": {
        "table": "1",
        "order_date": "2020-05-10",
        "order_by_name": "John",
        "order_by_email": "john@gmail.com",
        "additional_info": ""
    }
}
```

##### Response Success

```json
{
    "status": "OK",
    "data": {
        "id": 2,
        "created_at": "2020-05-08",
        "order_date": "2020-05-10",
        "additional_info": "",
        "order_by_name": "John",
        "order_by_email": "john@gmail.com",
        "table": 1
    }
}
```

##### Response Error (one of several)

```json
{
    "status": "FAIL",
    "errors": {
        "order_date": [
            "This field is required."
        ]
    }
}
```

## Tests

python -m pytest