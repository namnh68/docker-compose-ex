# docker-compose-ex
A simple application for Docker Compose

### How to run this application

**Step 1: Building images**

```
docker build -t app_web -f app.Dockerfile .
```

**Step 2: Running Redis container**

```
docker run -d --name redis-server -p 6379:6379 redis
```

**Step 3: Start App**

```
docker run -d --name webapp-server -p 5000:5000 \
--link redis-server:redis --env "REDIS_HOST=redis" --env "REDIS_PORT=6379" app_web
```

Done! Have fun