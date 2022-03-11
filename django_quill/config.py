DEFAULT_CONFIG = {
    "theme": "snow",
    "modules": {
        "table": True,
        "better-table": {
            "operationMenu": {
                "items": {
                    "unmergeCells": {
                        "text": 'Another unmerge cells name'
                    }
                },
                "color": {
                    "colors": ['green', 'red', 'yellow', 'blue', 'white'],
                    "text": 'Background Colors:'
                }
            }
        },
        "syntax": True,
        "toolbar": [
            [
                {"font": []},
                {"header": []},
                {"align": []},
                "bold",
                "italic",
                "underline",
                "strike",
                "blockquote",
                {"color": []},
                {"background": []},
            ],
            ["code-block", "link", "image", "video"],
            ["clean"],
        ],
        # quill-image-compress
        "imageCompressor": {
            "quality": 0.8,
            "maxWidth": 2000,
            "maxHeight": 2000,
            "imageType": "image/jpeg",
            "debug": False,
            "suppressErrorLogging": True,
        },
        # quill-resize
        "resize": {
            "showSize": True,
            "locale": {},
        },
        # quill-html-edit-button
        "htmlEditButton": {
            "syntax": True,
        }
    },
}
MEDIA_JS = [
    # syntax-highlight
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/languages/xml.min.js",
    # quill
    "https://cdn.quilljs.com/2.0.0-dev.2/quill.js",
    # quill-image-compress
    "https://cdn.jsdelivr.net/npm/quill-image-compress@1.2.21/dist/quill.imageCompressor.min.js",
    # quill-resize
    "https://cdn.jsdelivr.net/npm/@botom/quill-resize-module@2.0.0/dist/quill-resize-module.min.js",
    # quill-html-edit-button
    "https://unpkg.com/quill-html-edit-button@2.2.7/dist/quill.htmlEditButton.min.js",
    # custom
    "django_quill/django_quill.js",
]
MEDIA_CSS = [
    # syntax-highlight
    "https://cdn.quilljs.com/2.0.0-dev.2/quill.snow.css",
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/darcula.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/styles/github.min.css",
    # quill-resize
    "https://cdn.jsdelivr.net/npm/quill-resize-module@1.2.4/dist/resize.min.css",
    # custom
    "django_quill/django_quill.css",
]
