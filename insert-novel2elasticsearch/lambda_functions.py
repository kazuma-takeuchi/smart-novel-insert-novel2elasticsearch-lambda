import os
import json

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

from connection import build_client
from model import DEFAULT_BODY

ES_INDEX = os.getenv("ES_INDEX")
es = build_client()


def create_document(event):
    # TODO: 型チェック
    document = DEFAULT_BODY
    id_ = None
    if 'id' in event:
        id_ = event['id']
    document = event['document']
    if not isinstance(document['length'], int):
        document['length'] = None
    if 'like_count' in document and not isinstance(document['like_count'], int):
        document['like_count'] = 0
    return document, id_


def lambda_handler(event, context):
    document, id_ = create_document(event)
    print('BEGIN insert')
    res = es.index(index=ES_INDEX, id=id_, body=document)
    print(res)
    print('END insert')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
