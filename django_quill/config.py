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
        # quill-image-compress
        "imageCompressor": {
            "quality": 0.7,
            "maxWidth": 2000,
            "maxHeight": 2000,
            "imageType": "image/webp",
            "debug": False,
            "suppressErrorLogging": True,
        },
    },
}
