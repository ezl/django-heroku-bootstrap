rm data.db; python manage.py syncdb --noinput  --settings=settings.dev; python manage.py loaddata fixtures/adminuser.yaml --settings=settings.dev;
