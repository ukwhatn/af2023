#!/bin/bash
cd "$(dirname "$0")"

# frontend init
docker-compose build frontend
docker-compose run --rm frontend sh -c "cd /src && yarn create vite app --template react-ts"
