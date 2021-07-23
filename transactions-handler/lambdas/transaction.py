import json
import logging

logger = logging.getLogger(__name__)


def handler(event, context):
    logger.info('Event info: {event}'.format(event=event))

    if 'transaction' not in event:
        return {'statusCode': 400, 'message': 'No transaction info provided'}

    transaction_json = json.dumps({event['transaction']['id']: event['transaction']})
    return {
        'statusCode': 200,
        'transaction': transaction_json,
    }
