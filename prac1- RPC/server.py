# Yash Thakur (B-75)

from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    # Create server
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Server started. Waiting for client requests...")
    
    # Register the factorial function
    server.register_function(factorial, "factorial")
    
    # Run the server's main loop
    server.serve_forever()

if __name__ == "__main__":
    main()
