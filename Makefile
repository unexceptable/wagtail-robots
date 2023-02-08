test:
	@python testmanage.py test

run:
	@python testmanage.py runserver

user:
	@echo "Creating superuser - Username: test Password: test"
	@echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('test', '', 'test')" | python testmanage.py shell

migrate:
	@python testmanage.py migrate

tox-41:
	tox -e py38-dj41-wt41

tox-42:
	tox -e py38-dj42-wt42
