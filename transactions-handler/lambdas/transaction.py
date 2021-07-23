import json
import logging

logger = logging.getLogger(__name__)


def handler(event, context):
    logger.info('Event info: {event}'.format(event=event['body']))

    event_body = json.loads(event['body'])
    print(event_body)

    if 'transactions' not in event_body:
        return {'statusCode': 400, 'body': 'No transaction info provided'}

    return {
        'statusCode': 200,
        'body': json.dumps(event_body['transactions']),
    }
