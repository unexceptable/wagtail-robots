test:
	@python testmanage.py test

run:
	@python testmanage.py runserver

user:
	@echo "Creating superuser - Username: test Password: test"
	@echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('test', '', 'test')" | python testmanage.py shell

migrate:
	@python testmanage.py migrate

tox-215:
	tox -e py38-dj32-wt215

tox-216:
	tox -e py38-dj32-wt216

tox-3:
	tox -e py38-dj40-wt30

tox-4:
	tox -e py38-dj40-wt40
	tox -e py38-dj41-wt41
