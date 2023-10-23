
docker:
	docker build -t biotp .
	
run:
	docker run -v ${PWD}:/root/bio -w /root/bio --name bio_container -it biotp

start:
	docker start bio_container
	docker exec -it bio_container /bin/bash

stop:
	docker stop bio_container