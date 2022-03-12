.DEFAULT_GOAL = service

CURRENT_DIRECTORY = $(shell pwd)

# Компоненты
api:
	python manage.py start api

make-migration:
	python manage.py makemigration init_schema

migrate:
	python manage.py migrate up

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
