#!/usr/bin/env python3
import random
import math
import time
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def pollards_rho(n):
    x, y, c = random.randint(1, n - 1), random.randint(1, n - 1), random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (x ** 2 + c) % n
        y = (y ** 2 + c) % n
        y = (y ** 2 + c) % n
        d = gcd(abs(x - y), n)
    return d

def factorize(n):
    if n % 2 == 0:
        return 2, n // 2

    while True:
        d = pollards_rho(n)
        if d != n:
            return d, n // d

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./rsa <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    try:
        with open(file_path, 'r') as f:
            n = int(f.read().strip())
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    start_time = time.time()

    p, q = factorize(n)

    end_time = time.time()
    elapsed_time = end_time - start_time

    if p and q:
        print(f"{n}={p}*{q}")
        print(f"Time taken: {elapsed_time} seconds")
    else:
        print(f"Could not factorize {n} within 5 seconds.")
