django-ueditor-editor
========================================
django-ueditor-editor makes `UE.js` easy to use on Django Forms and admin sites

.. _UE.js: https://ueditorjs.com/

* **No configuration required for static files!**
* The entire code for inserting WYSIWYG editor is less than 30 lines
* It can be used in both admin and Django views

.. image:: ../_assets/django-ueditor-editor-sample.png


.. toctree::
   :maxdepth: 4
   :glob:

   pages/using-in-admin
   pages/using-as-form
   pages/using-as-modelform
   pages/change-toolbar-configs

Installation
************

Use pip to install from PyPI::

    pip install django-ueditor-editor

Add **django_ueditor** to **INSTALLED_APPS** in **settings.py**::

    INSTALLED_APPS = [
        'django.contrib.admin',
        ...
        'django_ueditor',
    ]

Contributing
************

To contribute to **django-ueditor-editor** `create a fork`_ on GitHub. Clone your fork, make some changes, and submit a pull request.

.. _create a fork: https://github.com/leehanyeong/django-ueditor-editor

Issues
******

Use the GitHub `issue tracker`_ for **django-ueditor-editor** to submit bugs, issues, and feature requests.

.. _issue tracker: https://github.com/leehanyeong/django-ueditor-editor/issues

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
