# Grafana

![GitHub Logo](/images/grafana.png)

## About
- StatsD, Graphite, and Grafana are three popular open-source tools used to aggregate and visualize metrics about systems and applications.
- Grafana is a powerful platform for monitoring and time-series data analysis. 
- Graphite is a system for data collection and visualization. 
- Graphite is strong in time-series metrics collection
- Grafana provides a more advanced solution for data analysis and visualization. 
- That’s why Graphite and Grafana are often used in a bundle.

## Info
- https://statsd.readthedocs.io/en/v3.2.1/reference.html
- https://grafana.com/docs/grafana/latest/administration/configuration/
- https://medium.com/swlh/create-grafana-dashboards-with-python-14a6962eb06c

## StatsD
StatsD is a simple daemon developed and released to aggregate and summarize application UDP metrics.The StatsD stack is one of the most popular monitoring solutions. StatsD is proving code examples for the Golang, NodeJS/Javascript and Python programming languages.

### Metrics
- UDP / TCP metric
- e.g. request reponse time
- each metric is its own bucket
- value (a.k.a "stat") provided by the metric is stored
- flushes occur at preset interval
- at flush, stats are aggregated and sent to an upstream backend service

## Graphite
### Components
- Carbon
- Whisper
- Graphite-Web

### Carbon
- Graphite storage backend
- carbon-cache
- listens for time-series data
- accepts metrics over several protocols

### Whisper
- DB / Library for storing time-series data
- "High resolution" > on recent data
- "Low resolution" > for historical data
- data stored in archives

e.g.

StatsD metric:
"email_sending.emails.sent"

is saved by Whisper file like this:
${WHISPER_ROOT}/email_sending/emails/sent.wsp

### Graphite-web
- Django Web App


## 1. Statsd Setup (Statsd data generating)
[More info ](https://github.com/yuyatinnefeld/docker/tree/master/grafana/statsd-setup)


## 2. Docker Grafana Setup (Data Visualization)
[More info ](https://github.com/yuyatinnefeld/docker/tree/master/grafana/docker-setup)


## 3. Local Grafana Setup (Data Visualization)
[More info ](https://github.com/yuyatinnefeld/docker/tree/master/grafana/grafana-setup)

## 4. Docker Grafana + Graphite Setup
[More info ](https://github.com/yuyatinnefeld/docker/tree/master/grafana/grafana_graphite-setup)
