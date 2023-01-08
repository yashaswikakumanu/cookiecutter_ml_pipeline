.PHONY: all install test

all: install test

install:
	conda env create -f environment.yaml
	conda activate mlops

test:
	pytest

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down
