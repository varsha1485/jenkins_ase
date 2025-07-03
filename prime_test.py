import sys

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
        if is_prime(num):
            print(f"{num} is a prime number.")
            sys.exit(0)  # Success
        else:
            print(f"{num} is not a prime number.")
            sys.exit(1)  # Failure
    except (IndexError, ValueError):
        print("Please provide a valid integer.")
        sys.exit(2)  # Invalid input
