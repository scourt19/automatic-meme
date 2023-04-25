#Makes you a superuser
#!/bin/bash
cd "$(dirname ${BASH_SOURCE[0]})"
source venv/bin/activate
cd website
python manage.py createsuperuser
