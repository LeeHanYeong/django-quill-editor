from collections.abc import Mapping

from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.renderers import get_default_renderer
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.utils.safestring import mark_safe

from .config import DEFAULT_CONFIG

__all__ = (
    'LazyEncoder',
    'QuillWidget',
)


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


json_encode = LazyEncoder().encode


class QuillWidget(forms.Textarea):
    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js',
            'django_quill/django_quill.js',
            'https://cdn.quilljs.com/1.3.6/quill.min.js',
        )
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/darcula.min.css',
                'django_quill/django_quill.css',
                'https://cdn.quilljs.com/1.3.6/quill.snow.css',
            )
        }

    def __init__(self, config_name='default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = DEFAULT_CONFIG.copy()
        configs = getattr(settings, 'QUILL_CONFIGS', None)
        if configs:
            if isinstance(configs, Mapping):
                if config_name in configs:
                    config = configs[config_name]
                    if not isinstance(config, Mapping):
                        raise ImproperlyConfigured('QUILL_CONFIGS["%s"] setting must be a Mapping object' % config_name)
                    self.config.update(config)
                else:
                    raise ImproperlyConfigured('No configuration named "%s" found in your QUILL_CONFIGS' % config_name)
            else:
                raise ImproperlyConfigured('QUILL_CONFIGS settings must be a Mapping object')

    def render(self, name, value, attrs=None, renderer=None):
        if renderer is None:
            renderer = get_default_renderer()
        if value is None:
            value = ''

        attrs = attrs or {}
        attrs['name'] = name
        if hasattr(value, 'quill'):
            attrs['quill'] = value.quill
        else:
            attrs['value'] = value
        final_attrs = self.build_attrs(self.attrs, attrs)
        return mark_safe(renderer.render('django_quill/widget.html', {
            'final_attrs': flatatt(final_attrs),
            'id': final_attrs['id'],
            'name': final_attrs['name'],
            'config': json_encode(self.config),
            'quill': final_attrs.get('quill', None),
            'value': final_attrs.get('value', None),
        }))
