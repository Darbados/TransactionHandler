import json
import logging
import boto3
from datetime import datetime

from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


s3 = boto3.client('s3')


def _save_transactions_json(transactions):
    try:
        # Save transaction into .json into S3 bucket

        s3.put_object(
            Bucket='transactions-storage-bucket-230721',
            Key='transaction_{}.json'.format(datetime.now().timestamp()),
            Body=bytes(json.dumps(transactions).encode('utf-8')),
        )
    except ClientError as e:
        return str(e)


def handler(event, _):
    logger.info('Event info: {event}'.format(event=event.get('body')))

    event_body = json.loads(event.get('body', {}))
    s3_error = _save_transactions_json(event_body.get('transactions'))

    if 'transactions' not in event_body:
        return {'statusCode': 400, 'body': 'No transaction info provided'}

    return {
        'statusCode': 200,
        'body': json.dumps({
            'transactions': event_body.get('transactions'),
            's3_error': s3_error,
        }),
    }
