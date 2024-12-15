#!/bin/sh

cd / && sh /setup_env_config.sh
md5=`md5sum /env-config.js | awk '{ print $1 }'`
file_name="env-config.${md5}.js"
mv /env-config.js /usr/share/nginx/html/${file_name}
sed -i 's/env-config.js/'$file_name'/g' /usr/share/nginx/html/index.html

exec "$@"
