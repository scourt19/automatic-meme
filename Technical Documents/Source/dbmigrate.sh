#Migrates all databases required
#!/bin/bash
cd "$(dirname ${BASH_SOURCE[0]})"
source venv/bin/activate
cd website
python3 manage.py migrate
