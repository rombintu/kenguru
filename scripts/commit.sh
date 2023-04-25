#!/bin/bash

set -eu

python3 -m poetry version patch
VERSION=$(cat pyproject.toml | head | grep version | cut -d '=' -f 2)
cp ./.gitignore ./.dockerignore
git add *
git commit -m $VERSION