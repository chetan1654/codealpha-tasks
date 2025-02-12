def fibonacci_generator(limit=None):
    """
    A generator function for the Fibonacci sequence.
    Yields Fibonacci numbers up to a specified limit if provided.
    """
    a, b = 0, 1
    count = 0
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == "__main__":
    fib = fibonacci_generator(10) 
    for num in fib:
        print(num)
