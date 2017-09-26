DOCKER = 'docker'
DOCKER_COMPOSE = 'docker-compose'
LAMBDA_PYTHON2 = 'lambci/lambda:python2.7'
LAMBDA_PYTHON3 = 'lambci/lambda:python3.6'
SRC_DIR = /dist/src

COMPOSE_FILE_BUILD = './build/docker-compose.yml'

clear-all: clear-con clear-img

clear-con:
	$(DOCKER) rm `$(DOCKER) ps -aq`

clear-img:
	$(DOCKER) rmi -f `$(DOCKER) images -aq`

build-up: dbuild up

lambda:
	$(DOCKER) run -v $(SRC_DIR):/var/task $(LAMBDA_PYTHON2) scrape.start_scrape

lambda3:
	$(DOCKER) run -v $(SRC_DIR):/var/task $(LAMBDA_PYTHON3) scrape.start_scrape

dbuild:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_BUILD) build

up:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE_BUILD) up 

down:
	$(DOCKER_COMPOSE) down
