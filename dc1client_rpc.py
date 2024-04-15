import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:8000/") as proxy:
    print('Connection Established')
    u_i = input('Enter no.: ')

    try:
        if not u_i:
            raise ValueError("No input provided")

        num = int(u_i)

        result = proxy.factorial(num)
        print(f"Factorial of {num}: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


