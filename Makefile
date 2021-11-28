setup_dev:
	cd testproject; ./start_development.sh

test:
	cd testproject; poetry install; \
		poetry run python manage.py test

publish:
	poetry publish --build