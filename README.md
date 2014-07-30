#NITT Smart Online Order System

Place your order conveniently from your hostel.

##To-do 

1. Display status-> order seen, order dispatched
2. Recommendation system
3. Complaint system : If too much time is exceeded since the order dispatch time then lodge a complaint

## How to run ?
Install `python2-virtualenv`
```
virtualenv2 flask
source flask/bin/activate
python2 db_create.py
python2 db_migrate.py
python2 runserver.py
```
