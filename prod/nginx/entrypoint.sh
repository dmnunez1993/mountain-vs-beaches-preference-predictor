#!/bin/sh

envsubst '${NGINX_BACKEND_PROXY} ${NGINX_BACKEND_HOST} ${NGINX_END_USER_PROXY} ${NGINX_END_USER_APP_HOST}' < /nginx.conf.template > /etc/nginx/conf.d/app.conf

exec "$@"
