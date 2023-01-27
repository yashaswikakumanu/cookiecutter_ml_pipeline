.PHONY: all install test

all: install test

install:
	conda install make
	conda config --add channels conda-forge
	conda create -n mlops
	conda activate mlops
	pip install -r requirements.txt
test:
	pytest

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down
