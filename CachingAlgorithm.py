from typing import List, Tuple, Set

import time

# Test cases
tests: List[Tuple[str, int]] = [
    ("0100001101001111", 999999),
    ("01000011010011110100110101010000", 999999),
    ("1111111111111111111111111111111111111111", 999999),
    ("010000110100111101001101010100000011000100111000", 999999999),
    ("01000011010011110100110101010000001100010011100000110001", 123456789012),
    ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345),
    ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678),
    ("01000011010011110100110101010000001100010011100000110001001110010010000101000001", 1234567890123456789),
    ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100", 12345678901234567890),
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890)
]

# Global cache for previously computed prime numbers
primes_cache: Set[int] = set()

def is_prime(x: int) -> bool:
    """
    Determine whether integer x is a prime number.

    //A prime number is a number greater than 1 that has no
    positive divisors other than 1 and itself

    x: The integer to check.
    return: True if x is prime, False otherwise.
    """
    # Quick checks for edge cases
    if x < 2:
        return False
    if x == 2:  # 2 is prime
        return True
    if x % 2 == 0:  # Exclude multiples of 2 > 2
        return False

    # Check for other divisors from 3 up to sqrt(x), skipping even numbers
    for i in range(3, int(x**0.5) + 1, 2):  # OPTIMIZED: Use range() instead of manual increment
        if x % i == 0:
            return False
    return True

def process_input(binary_string: str, num: int) -> None:
    """
    Process the binary string and find all unique primes less than N.
    Uses caching to speed up repeated calculations.
    """
    new_primes: Set[int] = set()

    # Generate all substrings of the binary string
    for i in range(len(binary_string)):
        for j in range(i + 1, len(binary_string) + 1):
            # Convert the current substring from binary to decimal
            val = int(binary_string[i:j], 2)

            # Check if val is < N and prime, then add to our cache
            if val < num and val not in primes_cache and is_prime(val):
                new_primes.add(val)

    # Update the global prime cache
    primes_cache.update(new_primes)

    count = len(primes_cache)
    if count == 0:
        print("0:")
        return  # OPTIMIZED: Avoid sorting when no primes found

    # Sort the unique primes in ascending order
    sorted_primes = sorted(primes_cache)

    # Output logic based on how many primes we found
    if count < 6:
        print(f"{count}: {', '.join(map(str, sorted_primes))}")
    else:
        print(f"{count}: {', '.join(map(str, sorted_primes[:3] + sorted_primes[-3:]))}")


def main():
    """Run the program multiple times, maintaining cache across runs."""
    for line in tests:
        binary_string: str = line[0]
        n: str = str(line[1])

        # Attempt to convert the integer part into an actual integer
        try:
            num: int = int(n)
        except ValueError:
            print("0: Invalid binary string")
            continue

        # Validate that the binary string contains only '0' or '1'
        if any(c not in '01' for c in binary_string):
            print("0: Invalid binary string")
            continue

        # Timing the execution
        start_time = time.time()
        process_input(binary_string, num)
        end_time = time.time()

        print(f"Execution Time: {end_time - start_time:.10f} seconds")

if __name__ == "__main__":
    main()
