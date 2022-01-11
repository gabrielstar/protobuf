#!/usr/bin/env bash

#create python client based on .proto files definition
protoc -I=$(pwd) --python_out=$(pwd) $(pwd)/addressbook.proto