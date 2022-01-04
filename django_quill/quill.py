import json

__all__ = (
    "QuillParseError",
    "Quill",
)

from django.utils.html import strip_tags


class QuillParseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Failed to parse value(%s)" % self.value


class Quill:
    def __init__(self, json_string):
        try:
            self.json_string = json_string
            json_data = json.loads(json_string)
            self.delta = json_data["delta"]
            self.html = json_data.get("html", "")
            self.plain = strip_tags(self.html).strip()
        except (json.JSONDecodeError, KeyError, TypeError):
            raise QuillParseError(json_string)
