# Backend

## Running instructions
### Install requirements:
```pip install -r requirements.txt```

### Run server:
```python manage.py runserver <IP>:<PORT>```

### Run all tests:
```python manage.py test```

htmlcov folder contains the coverage of the tests.

### Run coverage:
```coverage run --source='apiv1' manage.py test apiv1```

## Endpoints
### Ride-resource
| Ride | Methods | Endpoint |
| ------------- | ------------- | ------------- |
| rides | GET, POST |	/rides/	|
| passengers	|GET	| /rides/:pk/passengers/ |
| passenger	| GET, DELETE	| /rides/:pk/passengers/:pk/ |
| requests	| GET, POST	| /rides/:pk/requests/ |
| request	| POST	/rides/:pk/requests/:pk/accept/	|
| end a ride |	POST	/rides/:pk/end/	|

### User-resource	
| User | Methods | Endpoint |
| ------------- | ------------- | ------------- |
| users	| GET	| /users/	|
| profile |	GET, PUT, DELETE	| /users/:pk/ |

### Me-resource	
| Me | Methods | Endpoint |
| ------------- | ------------- | ------------- |
| ride requests made by current user |	GET	/me/requests/ |
| rides where current user passenger |	GET	| /me/rides-as-passenger/	|
| rides where current user driver	| GET	| /me/rides-as-driver/ |
| cars used by current user	| GET, POST	| /me/cars/ |
| car by current users	| GET, DELETE	| /me/:pk/cars/:pk/ |
