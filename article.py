
class Article:
    def __init__(self, data: dict):
        source_data = data.get('source', {})
        self.sourceId = source_data.get('id', None)
        self.sourceName = source_data.get('name', None)
        self.author = data.get('author', None)
        self.title = data.get('title', None)
        self.description = data.get('description', None)
        self.url = data.get('url', None)

    @staticmethod
    def from_json(json_response):
        # Assuming your JSON response is a dictionary
        return Article(json_response)