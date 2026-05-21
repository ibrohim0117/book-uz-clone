run:
	python3 manage.py runserver

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

secret_key:
	python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

admin:
	python3 manage.py createsuperuser