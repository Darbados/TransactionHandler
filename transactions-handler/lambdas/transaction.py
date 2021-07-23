import json
import logging

logger = logging.getLogger(__name__)


def handler(event, context):
    # logger.info('Event info: {event}'.format(event=json.dumps(event)))
    #
    # if 'transaction' not in event:
    #     return {'statusCode': 400, 'message': 'No transaction info provided'}
    #
    return {
        'statusCode': 200,
        'body': json.dumps(event['transaction']),
    }
