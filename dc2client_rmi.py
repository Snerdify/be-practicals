import Pyro5.api


def main():
    uri = "PYRONAME:string_concatenation_server"
    with Pyro5.api.Proxy(uri) as server:
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")

        result = server.concatenate_strings(str1, str2)
        print(f"Concatenation result: {result}")


if __name__ == "__main__":
    main()
