network = main_reseaux

all:
	docker network prune -f
	@docker network create $(network)
	@docker network ls
	docker compose up
