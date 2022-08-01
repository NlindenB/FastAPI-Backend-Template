#!/bin/bash

echo "Database connection --- Establishing"

while ! nc -z postgres 5432; do

    sleep 1

done

echo "Database connection --- Established"

exec "$@"