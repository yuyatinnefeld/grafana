# Grafana + Graphite

## create the docker-compose.yml

## stop the services
```bash
sudo systemctl stop statsd.service
sudo systemctl stop grafana-server
```


## docker setup

```bash
cd grafana_graphite
docker volume create --name=grafana-volume
docker-compose up -d
```

## add a new data source (graphite)

- localhost:3000
- Grafana > Configuration > Add data source
- Select Grahite
- URL: http://graphite:8080

## you can use the data source now


##

docker-compose down