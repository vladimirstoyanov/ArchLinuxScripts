docker network create my-net
docker run -d --name web --network my-net nginx
docker run -it --name client --network my-net busybox sh
