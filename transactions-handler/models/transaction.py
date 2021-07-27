""" Basic test of PynamoDB Model usage. """

from pynamodb.attributes import NumberAttribute, MapAttribute
from pynamodb.models import Model


class Transaction(Model):
    class Meta:
        table_name = 'transactions-dev'
        region = 'eu-west-3'
        host = 'https://dynamodb.eu-west-3.amazonaws.com'

    id = NumberAttribute(hash_key=True)
    amount = NumberAttribute()
    details = MapAttribute()
