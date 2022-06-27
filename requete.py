from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = client = Elasticsearch(
    "http://localhost:9200"
)

s = Search(using=client, index="question") \
    .filter("term", category="search") \
    .query("match", title="J'ai mal à l'os du bas")   \
    .exclude("match", description="beta")

s.aggs.bucket('per_tag', 'terms', field='tags') \
    .metric('max_lines', 'max', field='lines')

response = s.execute()

for hit in response:
    print(hit.meta.score, hit.title)

for tag in response.aggregations.per_tag.buckets:
    print(tag.key, tag.max_lines.value)