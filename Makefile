clean:
	find . -name "*.pyc" -exec rm -rf {} \;
run:
	python manage.py runserver 0.0.0.0:8000
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
user:
	python manage.py createsuperuser

shell:
	python manage.py shell