SHELL := bash
MAKEFLAGS += --warn-undefined-variables
.SHELLFLAGS := -euo pipefail -c
SUBMAKE_OPTS := -s

###############################################################################
# Configurable constants block
###############################################################################
DOCKER_PROJECT := zeroguard
DOCKER_IMAGE := zeroguard-api-docs
DOCKER_VERSION := 0.0.1

DOCKER_TAG := $(DOCKER_PROJECT)/$(DOCKER_IMAGE):$(DOCKER_VERSION)
DOCKER_RUN_OPTS := -it --rm -v `pwd`:/app -p 8000:8000

PIPENV_CMD_RUN := pipenv run
PIPENV_VENV := $(shell pipenv --venv)

SPHINX_SOURCE_DIR := ./docs
SPHINX_BUILD_DIR := $(SPHINX_SOURCE_DIR)/_build
SPHINX_CMD_BUILD := $(PIPENV_CMD_RUN) sphinx-build

# Due to some limitations of ReadTheDocs we need to manually copy static files
# of sphinxcontrib-httpexample plugin to a project static directory on each
# dependencies installation. See a relevant issue for more information:
# https://github.com/collective/sphinxcontrib-httpexample/issues/28
HTTPEX_STATIC := lib/python*/site-packages/sphinxcontrib/httpexample/static

###############################################################################
# Host targets
###############################################################################
.PHONY: all
all:
	$(MAKE) $(SUBMAKE_OPTS) ddev

.PHONY: dbuild
dbuild:
	docker build . -t $(DOCKER_TAG) -f Dockerfile

.PHONY: ddev
ddev: dbuild
	$(MAKE) $(SUBMAKE_OPTS) CMD='make dev' internal-drun

.PHONY: ddocs
ddocs: dbuild
	$(MAKE) $(SUBMAKE_OPTS) CMD='make docs' internal-drun

.PHONY: dkill
dkill:
	docker ps | grep $(DOCKER_TAG) | cut -f1 -d' ' | xargs docker kill

.PHONY: dsafeshell
dsafeshell: dbuild
	$(MAKE) $(SUBMAKE_OPTS) CMD='--shell' internal-drun

.PHONY: dshell
dshell: dbuild
	$(MAKE) $(SUBMAKE_OPTS) CMD='/bin/bash -i' internal-drun

###############################################################################
# Guest targets
###############################################################################
.PHONY: init
init:
	pip3 install pipenv --upgrade
	pipenv install --dev
	$(MAKE) $(SUBMAKE_OPTS) fixrtd

.PHONY: update
update:
	pipenv update --dev
	$(MAKE) $(SUBMAKE_OPTS) fixrtd

.PHONY: fixrtd
fixrtd:
	pipenv lock --requirements > requirements.txt
	cp $(PIPENV_VENV)/$(HTTPEX_STATIC)/* $(SPHINX_SOURCE_DIR)/_static

.PHONY: dev
dev:
	$(PIPENV_CMD_RUN) ./devserver.py

.PHONY: docs
docs:
	$(SPHINX_CMD_BUILD) $(SPHINX_SOURCE_DIR) $(SPHINX_BUILD_DIR)

###############################################################################
# Internal host targets
###############################################################################
.PHONY: internal-drun
internal-drun:
	docker run $(DOCKER_RUN_OPTS) $(DOCKER_TAG) $(CMD)

.PHONY: internal-dexec
internal-dexec:
	docker exec -it $(DOCKER_TAG) $(CMD)
