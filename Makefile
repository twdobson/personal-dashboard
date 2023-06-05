
.PHONY: clean
clean:
	find . -name '*.pyo' -delete
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	find . -name '*~' -delete
	find . -name '.coverage.*' -delete

.PHONY: run
run: 
	python manage.py runserver

.PHONY: migrate
migrate: 
	python manage.py makemigrations
	python manage.py makemigrations accounts
	python manage.py makemigrations authentication
	python manage.py makemigrations pastebin
	python manage.py migrate

.PHONY: shell
shell:
	python manage.py shell

.PHONY: create-super-user
create-super-user:
	python manage.py createsuperuser	
