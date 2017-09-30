DOCKER = 'docker'
DOCKER_COMPOSE = 'docker-compose'

COMPOSE_FILE_BUILD = './.build/docker-compose.yml'
COMPOSE_FILE_DEBUG = './.build/docker-compose.debug.yml'
COMPOSE_FILE_LAMBDA = './.docker-compose-lambda.yml'

LAMBDA_TEST_DATA = $(shell cat .lambda-test-data)

clear-all: clear-con clear-img

clear-con:
	$(DOCKER) rm `$(DOCKER) ps -aq`

clear-img:
	$(DOCKER) rmi -f `$(DOCKER) images -aq`

run: bundle lambda

rebuild: dbuild bundle
	
rebuildrun: dbuild bundle lambda

dbuild:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_BUILD) build

bundle:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_BUILD) -f $(COMPOSE_FILE_DEBUG) up

lambda:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_LAMBDA) up

lambda-req:
	$(DOCKER) run -v $(PWD)/dist/src:/var/task lambci/lambda:python2.7 scrape.start_scrape $(LAMBDA_TEST_DATA)

clean:
	sudo rm -rf ./dist/*
	sudo rm -rf ./virtualenv
