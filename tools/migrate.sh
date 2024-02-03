#!/bin/bash

echo "⚠️ Migrating database"
python3 manage.py migrate website zero
python3 manage.py makemigrations
python3 manage.py migrate
echo "✅ Database migrated"

python3 "$(pwd)/tools/create_products.py"

echo "🎉 All done!"
