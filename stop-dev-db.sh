ID=$(docker container ls | tail -1 | awk '{ print $1 }')
docker container rm -f $ID