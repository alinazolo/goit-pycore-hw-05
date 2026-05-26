def caching_fibonacci():
    # Cache stores already calculated Fibonacci numbers
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Return value from cache if it already exists
        if n in cache:
            return cache[n]

        # Calculate and save the result in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()

print(fib(10))
print(fib(15))
