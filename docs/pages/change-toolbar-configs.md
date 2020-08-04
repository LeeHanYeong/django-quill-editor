# Change toolbar config

> More settings can be found on the official site  
> https://quilljs.com/docs/modules/toolbar/

Add `QUILL_CONFIGS` to the **settings.py**

```python
QUILL_CONFIGS = {
    'default':{
        'theme': 'snow',
        'modules': {
            'syntax': True,
            'toolbar': [
                [
                    {'font': []},
                    {'header': []},
                    {'align': []},
                    'bold', 'italic', 'underline', 'strike', 'blockquote',
                    {'color': []},
                    {'background': []},
                ],
                ['code-block', 'link'],
                ['clean'],
            ]
        }
    }
}
```

