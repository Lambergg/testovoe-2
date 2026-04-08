1) Сборка образа бекенда \
docker build -t test_image  .

2) Создать докер сеть \
docker network create testNetwork

3) Создание образа БД \
docker run --name test_db \
-p 6432:5432 \
-e POSTGRES_USER=YOU_USER \
-e POSTGRES_PASSWORD=YOU_PASS \
-e POSTGRES_DB=Testovoe \
--network=testNetwork \
--volume pg-booking-data:/var/lib/postgresql/data \
-d postgres:16

4) Создание образа Redis \
docker run --name test_cache \
-p 7379:6379 \
--network=testNetwork \
-d redis:7.4

5) Запуск контейнера с приложением \
docker run --name test_back \
-p 8000:8000 \
--network=testNetwork \
test_image

#### Вставка моковых даннных в БД:
Выполнить команду:  \
docker exec test_back src/mock_data.py