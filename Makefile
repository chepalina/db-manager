.DEFAULT_GOAL = service

CURRENT_DIRECTORY = $(shell pwd)

# Компоненты
api:
	python manage.py start api

migration:
	export PYTHONPATH=$(CURRENT_DIRECTORY) \
	&& export FLASK_APP=$(CURRENT_DIRECTORY)/manage.py \
	&& flask db upgrade

# Unit тесты
unit-test:
	pytest ./tests

# Линтеры и форматеры
formatters-linters: black pylint pycodestyle mypy

black:
	black ./

pylint:
	pylint --rcfile=.pylintrc ./**/*.py

pycodestyle:
	pycodestyle ./

mypy:
	cd ../
	mypy $(CURRENT_DIRECTORY) --config-file=$(CURRENT_DIRECTORY)/mypy.ini
