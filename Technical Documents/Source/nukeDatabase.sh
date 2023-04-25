#!/bin/bash
cd "$(dirname ${BASH_SOURCE[0]})"
python3 -m venv venv
source venv/bin/activate
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate