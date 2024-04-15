import Pyro5.api


@Pyro5.api.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        result = str1 + str2
        return result


def main():
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns()

    uri = daemon.register(StringConcatenationServer)
    ns.register("string_concatenation_server", uri)

    print("Server is ready.")
    daemon.requestLoop()


if __name__ == "__main__":
    main()
