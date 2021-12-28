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
            ["code-block", "link", "image"],
            ["clean"],
        ],
        # ueditor-image-compress
        "imageCompressor": {
            "quality": 0.8,
            "maxWidth": 2000,
            "maxHeight": 2000,
            "imageType": "image/jpeg",
            "debug": False,
            "suppressErrorLogging": True,
        },
        # ueditor-image-resize
        "imageResize": {},
    },
}
MEDIA_JS = [
    "ueditor/ueditor.config.js",
    "ueditor/editor_api.js",
]
MEDIA_CSS = [
]
