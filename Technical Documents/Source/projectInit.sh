#Installs all dependencies in this directory.
#Sets up the Django project folder
#!/bin/bash
cd "$(dirname ${BASH_SOURCE[0]})"
rm -R venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
python3 -m pip install -r requirements.txt
