from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class Question(Document):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    # body = Text(analyzer='snowball')
    tags = Keyword()
    # published_from = Date()
    # lines = Integer()

    class Index:
        name = 'question'
        settings = {
          "number_of_shards": 1,
        }

    def save(self, ** kwargs):
        # self.lines = len(self.body.split())
        return super(Question, self).save(** kwargs)

    # def is_published(self):
    #     return datetime.now() > self.published_from

# create the mappings in elasticsearch
Question.init()

# create and save and article
question = Question(meta={'id': 1}, title='Je tousse, est-ce normal ?', tags=["toux", "gorge"])
# question.body = ''' looong text '''
# question.published_from = datetime.now()
question.save()

question = Question.get(id=42)
print(question.title())

# Display cluster health
print(connections.get_connection().cluster.health())