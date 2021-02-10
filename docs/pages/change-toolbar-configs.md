# Change toolbar config

> More settings can be found on the official site  
> https://quilljs.com/docs/modules/toolbar/

Add `QUILL_CONFIGS` to the **settings.py**

If you want to use inline style attributes (`style="text-align: center;"`) instead of class (`class="ql-align-center"`)
, set `useInlineStyleAttributes` to `True`.
It changes the settings only for `align` now. You can check the related
[Quill Docs](https://quilljs.com/guides/how-to-customize-quill/#class-vs-inline).


```python
QUILL_CONFIGS = {
    'default':{
        'theme': 'snow',
        'useInlineStyleAttributes': True,                   # uses inline style attributes (for align). https://quilljs.com/guides/how-to-customize-quill/#class-vs-inline
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
            ],
            'imageUploader': {
                'uploadURL': '/admin/quill/upload/',        # You can also use an absolute URL (https://example.com/3rd-party/uploader/)
                'addCSRFTokenHeader': True,
            }
        }
    }
}
```

