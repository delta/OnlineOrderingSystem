#NITT Smart Online Order System

Place your order conveniently from your hostel.

##To-do 

1. Display status-> order seen, order dispatched
2. Recommendation system
3. Complaint system : If too much time is exceeded since the order dispatch time then lodge a complaint

## How to run ?
```python
 python virtualenv.py flask
flask/bin/pip install flask==0.9
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail==0.7.6
flask/bin/pip install sqlalchemy==0.7.9
flask/bin/pip install flask-sqlalchemy==0.16
flask/bin/pip install sqlalchemy-migrate==0.7.2
flask/bin/pip install flask-wtf==0.8.4
flask/bin/pip install pytz==2013b
flask/bin/pip install flask-babel==0.8
flask/bin/pip install flup
flask/bin/pip install flask-whooshalchemy==0.55a
 ./db_create.py
 ./db_migrate.py
flask/bin/python runserver.py
```
