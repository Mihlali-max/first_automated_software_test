
class Post:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test content'}

        self.assertDiscEqual(expected, p.json)
