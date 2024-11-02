# bytehackz-discord-bot
A discord bot for bytehackz

## SETUP
### LOCAL
```
docker build -t <IMG_NAME> .
```

```
docker run --env-file .env --name <CONTAINER_NAME> <IMG_NAME>
```

### DEPLOY
- fly.io
  
```ps
Get-Content .env | flyctl secrets import
```

```sh
cat .env | fly secrets import
```

```
flyctl launch
```

```
flyctl deploy
```