from elasticsearch_dsl import Document, Text, Date, Integer, connections

# Подключаемся к Elasticsearch
connections.create_connection(hosts=['http://localhost:9200'],    headers={"Content-Type": "application/json"})
# Определяем тип документа для индексации
class PostDocument(Document):
    author = Text()
    content = Text()
    images = Text()  
    video = Text()   

    class Index:
        name = 'posts'

    def save(self, **kwargs):
        return super().save(**kwargs)
    