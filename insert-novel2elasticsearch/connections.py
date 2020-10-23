import os

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3


ES_HOST = os.getenv('ES_HOST')
ES_REGION = os.getenv('ES_REGION')
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, ES_REGION, service, session_token=credentials.token)

# host = 'vpc-smartnovel-es-dev-j74tj7mufmh6cmogkjcudm6uq4.ap-northeast-1.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
# region = 'ap-northeast-1' # e.g. us-west-1
# service = 'es'
# document = {
#     "title": "testnovel",
#     "author": "K.Takeuchi",
#     "description": "this is test."
# }
# es.index(index="smart-novel", doc_type="_doc", body=document)

def build_client(host=None):
    if host is None:
        host = ES_HOST
    
    es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )
    
    
    return es