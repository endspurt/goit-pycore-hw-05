def caching_fibonacci():
    # Create an empty dictionary to serve as the cache
    cache = {}
    
    def fibonacci(n):
        # Base case: return 0 for non-positive indices
        if n <= 0:
            return 0
        # Base case: return 1 for the first and second Fibonacci numbers
        elif n == 1:
            return 1
        # If the result is already cached, return it
        if n in cache:
            return cache[n]
        
        # Compute the Fibonacci number using recursion and store it in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    # Return the inner function
    return fibonacci
# Get the fibonacci function with caching
fib = caching_fibonacci()

# Use the fibonacci function to compute Fibonacci numbers
print(fib(10))  # Outputs 55
print(fib(15))  # Outputs 610
