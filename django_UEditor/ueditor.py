import json

__all__ = (
    "UEParseError",
    "UE",
)



class UEParseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Failed to parse value(%s)" % self.value


class UE:
    def __init__(self, json_string):
        try:
            self.json_string = json_string
            json_data = json.loads(json_string)
            self.delta = json_data["delta"]
            self.html = json_data.get("html", "")
        except (json.JSONDecodeError, KeyError, TypeError):
            raise UEParseError(json_string)
