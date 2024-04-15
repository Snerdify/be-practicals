import time


class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_server = 0

    def distribute_request(self, request):
        server = self.get_next_server()
        print(f"Request {request} sent to Server {server}")
        time.sleep(0.5)

    def get_next_server(self):
        next_server = self.current_server
        self.current_server = (self.current_server + 1) % len(self.servers)
        return self.servers[next_server]


def simulate_client_requests(load_balancer, num_requests):
    for i in range(1, num_requests + 1):
        load_balancer.distribute_request(i)


if __name__ == "__main__":
    server_addresses = ['Server A', 'Server B', 'Server C']
    load_balancer = LoadBalancer(server_addresses)

    simulate_client_requests(load_balancer, 10)
