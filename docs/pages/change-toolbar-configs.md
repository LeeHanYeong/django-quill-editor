# Change toolbar config

> More settings can be found on the official site  
> https://ueditorjs.com/docs/modules/toolbar/

Add `UEDITOR_CONFIGS` to the **settings.py**

```python
UEDITOR_CONFIGS = {
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

