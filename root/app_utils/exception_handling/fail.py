def fail(error) -> dict:
    data = {
        'status': False,
        'message': 'fail',
        'error': error
    }
    return data
