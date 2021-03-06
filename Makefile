# Include environment params reference
include make.env

.PHONY: build bash dev shell start restart stop rm

build:
	docker build --no-cache=true -t $(DOCKER_NAMESPACE)/$(DOCKER_REPOSITORY):$(DOCKER_IMAGE_VERSION) .

bash:
	docker exec -i -t $(DOCKER_CONTAINER_NAME) bash

dev:
	./enable-gui.sh && docker run --rm --name $(DOCKER_CONTAINER_NAME) -i -t $(DOCKER_PORTS) -v "$(shell pwd)$(DOCKER_MAPPED_VOLUMES)" -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$(IP):0 $(DOCKER_ENV) $(DOCKER_NAMESPACE)/$(DOCKER_REPOSITORY):$(DOCKER_IMAGE_VERSION) /bin/bash -c "pip install --trusted-host pypi.python.org -r requirements.txt && python src/app.py"

shell:
	./enable-gui.sh && docker run --rm --name $(DOCKER_CONTAINER_NAME) -i -t $(DOCKER_PORTS) -v "$(shell pwd)$(DOCKER_MAPPED_VOLUMES)" -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$(IP):0 $(DOCKER_ENV) $(DOCKER_NAMESPACE)/$(DOCKER_REPOSITORY):$(DOCKER_IMAGE_VERSION) /bin/bash

start:
	docker run -d --name $(DOCKER_CONTAINER_NAME) $(DOCKER_PORTS) $(DOCKER_ENV) $(DOCKER_NAMESPACE)/$(DOCKER_REPOSITORY):$(DOCKER_IMAGE_VERSION)

restart:
	docker start $(DOCKER_CONTAINER_NAME)

stop:
	docker stop $(DOCKER_CONTAINER_NAME)

rm:
	docker rm $(DOCKER_CONTAINER_NAME)

default: build
