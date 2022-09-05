# This script launches a docker instance

xhost +local:docker

docker-compose -f docker-compose.yaml run basic

docker-compose -f docker-compose.yaml stop basic
