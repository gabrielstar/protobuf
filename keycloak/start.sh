#!/usr/bin/env bash

set -e
cd server
#need to build our own image because there is no official image for arm64/linux Apple MacBook pro
docker build . -t keycloak:latest
port=10001
docker run --rm -d -p $port:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin keycloak:latest
sleep 5
open -a Safari http://localhost:$port/auth/admin