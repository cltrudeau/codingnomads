#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3

python manage.py wipe_migrations
python manage.py makemigrations core
python manage.py migrate
python manage.py create_test_admin
python manage.py create_test_data
