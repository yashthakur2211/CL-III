# Yash Thakur (B-75)

import xmlrpc.client

def main():
    # Connect to server
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    
    # Get integer input from user
    n = int(input("Enter an integer to compute factorial: "))
    
    # Call remote factorial function
    result = proxy.factorial(n)
    
    # Print the result
    print(f"Factorial of {n} is {result}")

if __name__ == "__main__":
    main()
