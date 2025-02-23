from typing import Any


def success(data: Any) -> dict:
    response = {
        'status': True,
        'message': 'success',
        'data': data
    }
