docker run -d -p 5432:5432 \
    -v todo-postgres-data:/Users/twiggy/Documents/fast_api_vue/postgres_data/ \
    --network todo-app \
    --network-alias postgres_container \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e POSTGRES_DB=db \
    library/postgres


#docker run -d \
#     --network todo-app --network-alias postgres_container \
#     -v todo-mysql-data:/var/lib/mysql \
#     -e MYSQL_ROOT_PASSWORD=secret \
#     -e MYSQL_DATABASE=todos \
#     mysql:5.7