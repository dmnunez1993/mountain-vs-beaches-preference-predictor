#!/bin/bash

# Recreate config file
rm -rf ./env-config.js
touch ./env-config.js

# Add assignment

if [[ -f .env.local ]]; then
    echo "Loading env file..."
    source .env.local
fi

if [[ ! -z "${API_ENDPOINT}" ]]; then
    echo "const ENV_API_ENDPOINT = \"${API_ENDPOINT}\";" >> env-config.js
else
    echo "const ENV_API_ENDPOINT = undefined;" >> env-config.js
fi

if [[ ! -z "${API_URL_SAME_ADDR}" ]]; then
    echo "const ENV_API_URL_SAME_ADDR = \"${API_URL_SAME_ADDR}\";" >> env-config.js
else
    echo "const ENV_API_URL_SAME_ADDR = undefined;" >> env-config.js
fi

if [[ ! -z "${API_URL_SAME_ADDR_PORT}" ]]; then
    echo "const ENV_API_URL_SAME_ADDR_PORT = \"${API_URL_SAME_ADDR_PORT}\";" >> env-config.js
else
    echo "const ENV_API_URL_SAME_ADDR_PORT = undefined;" >> env-config.js
fi
