import json

__all__ = (
    'QuillParseError',
    'Quill',
)


class QuillParseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Failed to parse value(%s)' % self.value


class Quill:
    def __init__(self, json_string):
        try:
            self.json_string = json.dumps(json_string)
            json_data = json_string
            self.delta = json_data['delta']
            self.html = json_data['html']
        except (json.JSONDecodeError, KeyError, TypeError):
            raise QuillParseError(json_string)
