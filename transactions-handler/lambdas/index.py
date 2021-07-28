def handler(event, context):
    query_string_parameters = event.get('queryStringParameters', {})
    if query_string_parameters:
        message = 'Index url returned {composed_message}'.format(
            composed_message=', '.join(query_string_parameters.values()))
    else:
        message = 'Index url has no GET parameters provided.'
    return {'statusCode': 200, 'body': f' {message}'}
