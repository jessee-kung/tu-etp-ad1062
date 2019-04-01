.DEFAULT_GOAL := build

# Modify this variable if your course git project is not located in the same directory as Makefile
COURSE_GIT_PROJECT ?= $(shell pwd)

# Modify this variable if you want the name the Docker Image in a different repository name or tag
IMAGE_NAME = tu-etp-ad1062:pynb

#### Do not modify area ####
NOTEBOOK_DIR = /home/jupyter/tu-etp-ad1062

build:
	docker build --rm -t $(IMAGE_NAME) - < Dockerfile

start: build
	docker run -d --rm --name pynb -p 8888:8888 --mount type=bind,src=$(COURSE_GIT_PROJECT),dst=$(NOTEBOOK_DIR) -w $(NOTEBOOK_DIR) $(IMAGE_NAME)
	sleep 2
	docker logs pynb

stop:
	docker stop pynb

clean:
	docker rmi $(IMAGE_NAME)

#### Do not modify area ####
