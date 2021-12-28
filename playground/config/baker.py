import json

from django.utils.functional import LazyObject
from model_bakery import baker as default_baker

__all__ = ("baker",)


class LazyBaker(LazyObject):
    @staticmethod
    def _gen_ueditor_field():
        return json.dumps(
            {
                "delta": {
                    "ops": [
                        {"insert": "Django", "attributes": {"bold": True}},
                        {"insert": " UE "},
                        {
                            "insert": "Editor",
                            "attributes": {"bold": True, "color": "#ff0000"},
                        },
                    ]
                },
                "html": '<p><strong>Django</strong> UE <strong style="color: #ff0000;">Editor</strong></p>',
            }
        )

    def _setup(self):
        default_baker.generators.add(
            "django_ueditor.fields.UEField", self._gen_ueditor_field
        )
        self._wrapped = default_baker


baker = LazyBaker()
