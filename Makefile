SHELL := /bin/bash

start_env:
	source ./.venv/bin/activate

hd-ls:
	hadoop dfs -ls /

run:
	PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python python3 main.py

init:
	poetry init

install:
	poetry install
	# poetry install --no-root (no dev)

test:
	python -m unittest discover -s ./tests -p '*_test.py'

.PHONY: test
