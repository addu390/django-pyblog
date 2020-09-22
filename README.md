# Django Pyblog `Work In Progress 🚁`
Django blog - ElasticSearch + MySQL + Redis 🚀

#### Why?
- Most of us use wordpress 🥱 for blogs (so do I: https://pyblog.xyz). The search operation in wordpress takes forever, because it's a simple `column like '%<complete input string>%` 🤕
- To perform faster search operations on tags, categories and other key-words. While it can be achieved with Relational and other NoSQL data stores, Elastic Search is the best when it comes to `SEARCH` 😎

#### Installation ElasticSearch (MacOS)
- Tap the Elastic Homebrew repository: `brew tap elastic/tap`
- `brew install elastic/tap/elasticsearch-full`
- `pip install elasticsearch-dsl`

#### Start the Server
- `cd /usr/local/var/homebrew/linked/elasticsearch-full/bin`
- `./elasticsearch`
To start ES from GUI, follow: https://opensource.com/article/19/7/installing-elasticsearch-macos

#### Test ES Set-up
- `curl -XGET http://localhost:9200`
Expected Response (Similar):
```
{
    "name": "PP-C02Z66CALVCG.local",
    "cluster_name": "elasticsearch_adesh.nalpet",
    "cluster_uuid": "E_543bFmSUqO7dXwzjE1WQ",
    "version": {
        "number": "7.8.1",
        "build_flavor": "default",
        "build_type": "tar",
        "build_hash": "b5ca9c58fb664ca8bf9e4057fc229b3396bf3a89",
        "build_date": "2020-07-21T16:40:44.668009Z",
        "build_snapshot": false,
        "lucene_version": "8.5.1",
        "minimum_wire_compatibility_version": "6.8.0",
        "minimum_index_compatibility_version": "6.0.0-beta1"
    },
    "tagline": "You Know, for Search"
}
```

#### Installation Redis (MacOS)
- `brew install redis`
- `brew services start redis` or `redis-server /usr/local/etc/redis.conf`
- `pip install django-redis`

#### Test Redis Set-up
- `redis-cli ping`

For details on how to set-up a django project with best practices: https://pyblog.xyz/django-initial-setup/

#### Settings
- Update ES and Redis - host and port in `settings.py` 
```
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}
```
```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "pyblog"
    }
}
```

#### Updating the Index
- bulk indexing: `search.bulk_indexing`
- On every `post_save`: `signals.py`
More details on Django Signals: https://pyblog.xyz/events-using-django-signals/

#### Template Used
[Blog Home](https://startbootstrap.com/templates/blog-home/) is a basic blog homepage HTML starter template for [Bootstrap](https://getbootstrap.com/) created by [Start Bootstrap](https://startbootstrap.com/).

[![Blog Home Preview](https://startbootstrap.com/assets/img/screenshots/templates/blog-home.png)](https://startbootstrap.github.io/startbootstrap-blog-home/)

**[View Live Preview](https://startbootstrap.github.io/startbootstrap-blog-home/)**

###### Note: The project is obviously over-engineered, it's meant to give an example on how versatile Django can be 😋 
