web: daphne server.asgi:application -p $PORT -b 0.0.0.0 -v2
worker: python manage.py runworker --settings=server.settings -v2