DOCKER = 'docker'
DOCKER_COMPOSE = 'docker-compose'

COMPOSE_FILE_BUILD = './.build/docker-compose.yml'
COMPOSE_FILE_LAMBDA = './.docker-compose-lambda.yml'

clear-all: clear-con clear-img

clear-con:
	$(DOCKER) rm `$(DOCKER) ps -aq`

clear-img:
	$(DOCKER) rmi -f `$(DOCKER) images -aq`

rebuild: dbuild bundle
	
rebuildrun: dbuild bundle lambda

dbuild:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_BUILD) build

bundle:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_BUILD) up 

lambda:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_LAMBDA) up

full: bundle lambda
