DOCKER = 'docker'
DOCKER_COMPOSE = 'docker-compose'

COMPOSE_FILE_BUILD = './build/docker-compose.yml'

clear-all: clear-con clear-img

clear-con:
	$(DOCKER) rm `$(DOCKER) ps -aq`

clear-img:
	$(DOCKER) rmi -f `$(DOCKER) images -aq`

build-up: dbuild up

dbuild:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_BUILD) build

up:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_BUILD) up 

down:
	$(DOCKER_COMPOSE) down
