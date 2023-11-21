# Config Macro :
network = main_reseaux

# Colors :
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
ORANGE='\033[0;33m'
W='\033[0m'

id = " "

# Rules 

re: stop run

run : run_src see

stop:
	@echo ${RED}** STOP **${W}
	docker network prune -f
	docker compose down

see:
	@echo ${YELLOW}** SEE **${W}
	@echo "Liste of container run"
	@docker ps
	@echo "Liste of network"
	@docker network ls
id:
	@echo ${ORANGE}** SHOW ID**${W}
	@docker ps --format "{{.ID}}: {{.Names}}"
# Do this target like this << make connect id=00e38585718d >> (It's an example of course ...)
connect:
	@docker exec -t ${id} /bin/sh
# UTILS

net:
	@docker network create $(network)
	@docker network ls

run_src: 
	@echo ${GREEN}** RUN **${W}
	@make net
	docker compose up -d

