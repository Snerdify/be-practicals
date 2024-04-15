import time
import random


class DynamicLoadBalancer:
    def __init__(self, servers):
        self.servers = {server: 0 for server in servers}

    def distribute_request(self, request):
        min_load_server = min(self.servers, key=self.servers.get)
        print(f"Request {request} sent to Server {min_load_server}")
        time.sleep(0.5)
        self.servers[min_load_server] += 1

    def display_server_loads(self):
        print("Current server loads:")
        for server, load in self.servers.items():
            print(f"Server {server}: {load}")


def simulate_dynamic_load_balancing(load_balancer, num_requests):
    for i in range(1, num_requests + 1):
        load_balancer.distribute_request(i)
        if i % 5 == 0:
            load_balancer.display_server_loads()


if __name__ == "__main__":
    server_addresses = ['Server B', 'Server A', 'Server C']
    dynamic_load_balancer = DynamicLoadBalancer(server_addresses)

    simulate_dynamic_load_balancing(dynamic_load_balancer, 20)
