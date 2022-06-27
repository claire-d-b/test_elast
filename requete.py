from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = client = Elasticsearch(
    "http://localhost:9200"
)

s = Search(using=client, index="question") \
    .query("match", title="J'ai mal à l'os du bas")   \

s.aggs.bucket('per_tag', 'terms', field='tags') \
    .metric('max_lines', 'max', field='lines')

response = s.execute()

for hit in response:
    print(hit.meta.score, hit.title)

for tag in response.aggregations.per_tag.buckets:
    print(tag.key, tag.max_lines.value)

s2 = Search(using=client, index="question") \
    .query("match", tags="J'ai mal à l'os du bas")   \

s2.aggs.bucket('per_tag', 'terms', field='tags') \
    .metric('max_lines', 'max', field='lines')

response2 = s2.execute()

for hit in response2:
    print(hit.meta.score, hit.title)

for tag in response2.aggregations.per_tag.buckets:
    print(tag.key, tag.max_lines.value)