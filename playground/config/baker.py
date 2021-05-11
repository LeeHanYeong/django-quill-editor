import json

from django.utils.functional import LazyObject
from model_bakery import baker as default_baker

__all__ = ("baker",)


class LazyBaker(LazyObject):
    @staticmethod
    def _gen_quill_field():
        return json.dumps(
            {
                "delta": {
                    "ops": [
                        {"insert": "Django", "attributes": {"bold": True}},
                        {"insert": " Quill "},
                        {
                            "insert": "Editor",
                            "attributes": {"bold": True, "color": "#ff0000"},
                        },
                    ]
                },
                "html": '<p><strong>Django</strong> Quill <strong style="color: #ff0000;">Editor</strong></p>',
            }
        )

    def _setup(self):
        default_baker.generators.add(
            "django_quill.fields.QuillField", self._gen_quill_field
        )
        self._wrapped = default_baker


baker = LazyBaker()
