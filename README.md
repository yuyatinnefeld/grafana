# Grafana & Graphite
StatsD, Graphite, and Grafana are three popular open-source tools used to aggregate and visualize metrics about systems and applications.

## StatsD
StatsD is a simple daemon developed and released to aggregate and summarize application UDP metrics.The StatsD stack is one of the most popular monitoring solutions. StatsD is proving code examples for the Golang, NodeJS/Javascript and Python programming languages.

### Metrics
- UDP / TCP metric
- e.g. request reponse time
- each metric is its own bucket
- value (a.k.a "stat") provided by the metric is stored
- flushes occur at preset interval
- at flush, stats are aggregated and sent to an upstream backend service

## Setup
```bash
sudo apt-get -y update
sudo apt-get -y install git node.js devscripts debhelper npm dh-systemd
```
