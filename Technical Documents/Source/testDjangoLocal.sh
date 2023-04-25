#Lauches the web application on 127.0.0.1:8080
#I hope everyone is on OSX else { Write another command script }
#run local env setup before using this script
#!/bin/bash
cd "$(dirname ${BASH_SOURCE[0]})"
source venv/bin/activate
python3 import django
python3 import pillow
cd website
python3 manage.py runserver