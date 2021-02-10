
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
    def __init__(self, data):
        assert isinstance(data, dict), (
            "Quill expects dictionary as data but got %s(%s)." % (type(data), data)
        )
        self.data = data
        try:
            self.delta = data['delta']
            self.html = data['html']
        except (KeyError, TypeError):
            raise QuillParseError(data)
