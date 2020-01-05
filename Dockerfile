FROM	python:3.6-buster
RUN	pip install pipenv
COPY	app/* /app/
COPY	Pipfile* /tmp/
RUN     cd /tmp && pipenv lock --requirements > requirements.txt
RUN     pip install -r /tmp/requirements.txt
WORKDIR	/app
ENV		SHELL=/bin/bash
CMD		["python3", "app.py"]
