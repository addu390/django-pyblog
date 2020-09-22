from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date, Search, Boolean, Integer
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class PostIndex(Document):
    author = Text()
    post_id = Text()
    is_active = Boolean()
    title = Text()
    category = Text()
    description = Text()
    created_at = Date()
    updated_at = Date()

    class Index:
        name = 'post-index'


def bulk_indexing():
    PostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Post.objects.all().iterator()))


def search_match(description):
    s = Search().filter('match', description=description)[:5]
    response = s.execute()
    return response


def search_term(category):
    s = Search().filter('term', category=category)[:5]
    response = s.execute()
    return response
