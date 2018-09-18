Install requirements:
- pip install -r requirements.txt

Run server:
- python manage.py runserver <IP>:<PORT>

Run all tests:
- python manage.py test

htmlcov folder contains the coverage of the tests.

Run coverage:
- coverage run --source='apiv1' manage.py test apiv1