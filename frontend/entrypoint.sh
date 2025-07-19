#!/bin/sh
set -e

if [ ! -d node_modules ] || [ -z "$(ls -A node_modules 2>/dev/null)" ]; then
  echo "Node modules missing, installing dependencies..."
  npm install
fi

exec npm run dev -- --host
