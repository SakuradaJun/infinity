# Infinity

Install psql (PostgreSQL) 10.1, `createdb infinity`

`git clone git@github.com:infamily/infinity.git`

Then:

```
cd infinity
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver
```
_Note, that whatever user you create, the username is set to username_hash(self.email), e.g.:_

```python
>>> from oo.users.models import username_hash
>>> username_hash('admin@admin.com')
Admin@D3942DCE
```


Apply fixtures:

```
python manage.py loaddata languages
python manage.py loaddata types instances
python manage.py loaddata currencies currency_price_snapshots hour_price_snapshots
```

Run tests:

`py.test`

