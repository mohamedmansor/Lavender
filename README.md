# Lavender

Lavender is a python App for an online flower store. The project have `garden` that have flowers and categories.

## Installation

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ nano .env
```
add data bellow to `.env` file. with your own values.
```bash
SECRET_KEY=<SERCRET_KEY>

DB_NAME=<db_name>
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_HOST=<db_host>
```

## Usage

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)