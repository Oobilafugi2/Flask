#!/bin/sh

# needed to change CRLF to LF to read linux shell
# waits for postgres to start
echo "Waiting for postgres..."

while ! nc -z api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# sets flask app (not sure if I need this)
export FLASK_APP=src/__init__.py

# runs app with python
python manage.py run -h 0.0.0.0