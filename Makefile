.SILENT:

pythonpath := $(PWD)
pythonpath := $(pythonpath):$(PWD)/tests
pythonpath := $(pythonpath):$(PWD)/app

run:
	docker-compose up -d deployment-service

build:
	docker-compose build deployment-service

test:
	PYTHONPATH=$(pythonpath) pytest tests

migrate:
	alembic upgrade head

migrate-down:
	alembic downgrade -1

current-migration:
	alembic current

install-dev:
	pip3 install -r ./requirements/dev.txt

install-test:
	pip3 install -r ./requirements/test.txt

install-lint:
	pip3 install -r ./requirements/lint.txt