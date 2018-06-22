#!/bin/bash

# Prepare log files and start outputting logs to stdout
touch /app/logs/diff_generator_gunicorn.log
touch /app/logs/diff_generator_access.log
tail -n 0 -f /app/logs/diff_generator_*.log &

python3 manage.py collectstatic
python3 manage.py migrate

exec gunicorn diff_generator.wsgi:application \
    --name diff_generator \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/app/logs/diff_generator_guinicorn.log \
    --access-logfile=/app/logs/diff_generator_access.log \
"$@"