import os
import json

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

from connections import build_client
from models import DEFAULT_DOCUMENT, NovelModel

ES_INDEX = os.getenv("ES_INDEX")
es = build_client()


def lambda_handler(event, context):
    document = NovelModel(**event["document"]).dict()
    id_ = event["id"]
    print(f'id ={id_}, doc={document}')
    print('BEGIN insert')
    res = es.index(index=ES_INDEX, id=id_, body=document)
    print(res)
    print('END insert')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
