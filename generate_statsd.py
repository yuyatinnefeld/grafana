import random
import statsd
import time

HOST = 'localhost'
PORT = 8125

client = statsd.StatsClient(HOST, PORT)


def server_1_CPU(random_num_CPU):
    client.incr('server-aa.CUP', random_num_CPU)

def server_2_CPU(random_num_CPU):
    client.incr('server-bb.CUP', random_num_CPU)

def server_1_RAM(random_num_RAM):
    client.incr('server-aa.RAM', random_num_RAM)

def server_2_RAM(random_num_RAM):
    client.incr('server-bb.RAM', random_num_RAM)


if __name__ == "__main__":

    while True:
        random.seed()
        random_num_CPU = random.randint(0, 10)
        random_num_RAM = random.randint(0, 10)

        if random_num_CPU > 5:
            print('server 1 CPU used: {}'.format(random_num_CPU))
            server_1_CPU(random_num_CPU)

        if random_num_CPU < 7:
            print('server 2 CPU used: {}'.format(random_num_CPU))
            server_2_CPU(random_num_CPU)

        if random_num_RAM > 2:
            print('server 1 RAM used: {}'.format(random_num_RAM))
            server_1_RAM(random_num_RAM)

        if random_num_RAM < 7:
            print('server 2 RAM used: {}'.format(random_num_RAM))
            server_2_RAM(random_num_RAM)

        time.sleep(2)
