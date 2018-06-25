#!/bin/bash -e
j2 /var/www/difffify/nginx.conf.j2 \
   > /etc/nginx/conf.d/default.conf

until nginx -g "daemon off;error_log stderr;"; do
    echo "Server 'myserver' crashed with exit code $?.  Respawning.." >&2
    sleep 1
done

