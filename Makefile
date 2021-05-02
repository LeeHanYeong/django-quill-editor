test:
	cd testproject; poetry install; \
		poetry run python manage.py test

publish:
	poetry publish --build