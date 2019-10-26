build:
	rm -rf dist/ build/
	python3 setup.py sdist bdist_wheel

install: build 
	pip3 install dist/ceres*.whl

build_docker: build
	docker build -t ceres .

run: build
	docker run -it --rm -v $(PWD)/example/:/example --name ceres ceres /bin/bash

test: build
	rm -f example/*.py
	docker run -it --rm --name ceres ceres /usr/bin/python3 -m ceres example/

clean:
	rm -rf dist/ build/
	docker images | grep "<none>" | grep -o -E "[0-9a-f]{12,12}" |xargs docker rmi -f