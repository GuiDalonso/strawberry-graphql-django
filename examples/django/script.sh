poetry run ./manage.py makemigrations
poetry run ./manage.py migrate
poetry run ./manage.py loaddata berries
poetry run ./manage.py runserver