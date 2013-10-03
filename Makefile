PYTHON_BIN=python
PIP_BIN=pip
MANAGE_FILE=to_be_a_musician/manage.py
REQUIREMENTS_FILE=requirements-dev.txt


help:
	@echo 'Makefile for To Be Musician project										'
	@echo '																			'
	@echo 'Usage:																	'
	@echo '   make setup    install dependencies and execute migrations				'
	@echo '   make run      run Django built-in server								'
	@echo '   make test     run all or specific app tests							'


setup:
	@$(PIP_BIN) install -r $(REQUIREMENTS_FILE)
	@$(PYTHON_BIN) $(MANAGE_FILE) syncdb --migrate

run:
	@$(PYTHON_BIN) $(MANAGE_FILE) runserver

test:
	@$(PYTHON_BIN) $(MANAGE_FILE) test $(app)
