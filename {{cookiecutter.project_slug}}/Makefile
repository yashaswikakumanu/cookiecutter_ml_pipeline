CONDA_ENV=mlops
# https://stackoverflow.com/questions/53382383/makefile-cant-use-conda-activate

SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

.PHONY: all install test

all: install test

install:
# create conda env from environemt.yml file
	@echo "Creating conda environment for $(CONDA_ENV)..."
	conda create -n $(CONDA_ENV) -y python=3.10

test:
	@$(CONDA_ACTIVATE) $(CONDA_ENV) && \
	pytest

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

clean:
	conda env remove -n $(CONDA_ENV);

