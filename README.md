# Example Flask Server with Migration, ORM and views

This is a simple flask server that is ready for deploy to a plethora of services.  Should work on heroku, PaaS et al.

Also should be quickly deployable to AWS, with minor alterations.


## Steps for setup

### On Mac OSX 

#### Create database - on OS

`createuser -P -s -d -e basic_admin`

`createdb example_db -U basic_admin`

#### Create database - on Flask

`python create_db.py`

#### Set up migrations

`python manage.py db init`

`python manage.py db migrate`

`python manage.py db upgrade`

### Runing the application

`honcho start`

### message passing

```
import requests
import json
requests.post("http://localhost:5000/route2", headers={'Content-Type': 'application/json'}, data=json.dumps({"whatever": "thing"}))
```

^^^ pass in the above to test the given route.  Notice in the route you need `request.get_json()`
