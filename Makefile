PYTHON_BIN=python
PIP_BIN=pip
MANAGE_FILE=to_be_a_musician/manage.py
REQUIREMENTS_FILE=requirements-dev.txt
COMPASS_PATH=to_be_a_musician/common/


help:
	@echo 'Makefile for To Be Musician                                              '
	@echo '                                                                         '
	@echo 'Usage:                                                                   '
	@echo '   make setup    install dependencies and execute migrations             '
	@echo '   make run      run Django built-in server                              '
	@echo '   make compass  start compass watching for styles alterations           '
	@echo '   make test     run all or specific app tests                           '


setup:
	@$(PIP_BIN) install -r $(REQUIREMENTS_FILE)
	@$(PYTHON_BIN) $(MANAGE_FILE) syncdb --migrate

run:
	@$(PYTHON_BIN) $(MANAGE_FILE) runserver

compass:
	@cd $(COMPASS_PATH) && compass watch

test:
	@$(PYTHON_BIN) $(MANAGE_FILE) test $(app)
