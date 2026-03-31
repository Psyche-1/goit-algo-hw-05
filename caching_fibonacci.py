def caching_fibonacci():
    """Function that caching calculated value"""
    cache: dict[int, int]  = dict()

    def fibonacci(n: int) -> int:
        """Function that calculate fibonacci number using cache"""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()

print(fib(10))
print(fib(15))
