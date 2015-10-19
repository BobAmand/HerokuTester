## Instructions

Download the contents of this repository to your chosen directory.

Run (starting at the base, where this README is located):
- ```echo layout python3 >> .envrc```
- ```direnv allow```
- ```pip install -r requirements.txt```
- ```cd urlybird```
- ```python manage.py migrate```
- ```python manage```
- ```python manage.py generate_data``` << only if you want to generate fake data
- ```python manage.py runserver```

Then, open this in your browser:

[localhost:8000](localhost:8000)
