DEFAULT_CONFIG = {
    "theme": "snow",
    "modules": {
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
    },
}
MEDIA_JS = [
    # syntax-highlight
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js",
    # quill
    "https://cdn.quilljs.com/1.3.7/quill.min.js",
    # quill-image-compress
    "https://cdn.jsdelivr.net/npm/quill-image-compress@1.2.21/dist/quill.imageCompressor.min.js",
    # quill-resize
    "https://cdn.jsdelivr.net/npm/@botom/quill-resize-module@2.0.0/dist/quill-resize-module.min.js",
    # custom
    "django_quill/django_quill.js",
]
MEDIA_CSS = [
    # syntax-highlight
    "https://cdn.quilljs.com/1.3.7/quill.snow.css",
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/darcula.min.css",
    # quill-resize
    "https://cdn.jsdelivr.net/npm/quill-resize-module@1.2.4/dist/resize.min.css",
    # custom
    "django_quill/django_quill.css",
]
