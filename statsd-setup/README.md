# StatsD Setup

## install statsD

install packages
```bash
sudo apt-get -y update
sudo apt-get -y install git nodejs devscripts debhelper npm dh-systemd
```

clone statsd.git
```bash
cd /tmp/
git clone https://github.com/statsd/statsd.git
```

build dev

```bash
cd statsd/
sudo dpkg-buildpackage
cd ..
```

you can see the statsd package now
```bash
$ ls
...
statsd
statsd_0.9.0-1_all.deb
statsd_0.9.0-1_amd64.buildinfo
statsd_0.9.0-1_amd64.changes
statsd_0.9.0-1.dsc
statsd_0.9.0-1.tar.gz

```
install statsd and activate and stop
```bash
sudo dpkg -i statsd_0.9.0-1_all.deb
sudo systemctl start statsd.service
sudo systemctl status statsd.service
sudo systemctl stop statsd.service
```

## configure StatsD

```bash
sudo -s
vim /etc/statsd/localConfig.js
```

activate debug
```bash
{
//  graphitePort: 2003
//, graphiteHost: "localhost"
  debug: "True"
, port: 8125
}
```

restart the statsd.service
```bash
sudo systemctl start statsd.service
```

sent a message to statsd
```bash
echo "foo:1|c" | nc -u -w0 127.0.0.1 8125

```

## StatsD Type of metrics
```bash
<bucket>:<value>|<metric_type>
```

### Types
- Counters
- Timers
- Gauges
- Sets

#### Counters
```bash
email_sending.emails.sent:300|c
```
- Bucket:email_sending.emails.sent
- Value: 300
- Counter: c

#### Timer
```bash
email_sending.emails.sent:560|ms
```
- Timer: ms

#### Gauge
- not automatically reset on a per-flush basis


```bash
email_sending.render.num_recommendations:5|g

# add a sign (+/-) to change instead of set the value
email_sending.render.num_recommendations:+1|g
email_sending.render.num_recommendations:-1|g

```
- Gauge: g

#### Sampling
```bash
email_sending.render.num_recommendations:560|ms|@0.1
```
- Sampling 10 %: @0.1