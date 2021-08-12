# Grafana Docker Setup

## add StatsD to an application

```bash
# you need stop statsd.service because of the using port
sudo systemctl stop statsd.service

docker run -id -p 8000:8000 -p 3000:3000 -p 8125:8125/udp kamon/grafana_graphite
docker ps
```

## create data generator
```bash
sudo pip install statsd
vi statsd_script.py
```

## send the data to statsd
```bash
python statsd_script.py
Got random interval to sleep: 13
Got random interval to sleep: 10
Got random interval to sleep: 6

```
## Grafana Web Interface

### open localhost:3000 

### login
-user: admin
-password: admin

### create a dashboard
- New Dashboard
- Edit
- stats, counter, statsd_script, sleep_calls, count
- Last 15 Min
![GitHub Logo](/images/grafana.png)
