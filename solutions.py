from typing import Dict, List, Set


# Numbers

def list_square(li: List[float]) -> List[float]:
    squares = []
    for x in li:
        squares.append(x ** 2)
    return squares


def list_max(li: List[float]) -> float:
    max_val = li[0]
    for x in li:
        if x > max_val:
            max_val = x
    return max_val


def list_min(li: List[float]) -> float:
    min_val = li[0]
    for x in li:
        if x < min_val:
            min_val = x
    return min_val


def list_mean(li: List[float]) -> float:
    total = 0
    for x in li:
        total += x
    return total / len(li)


def list_stddev(li: List[float]) -> float:
    mean = list_mean(li)
    variance = 0
    for x in li:
        variance += (mean - x) ** 2 / len(li)
    return variance ** 0.5


def is_prime(n: int) -> bool:
    for f in range(2, int(n ** 0.5) + 1):
        if n % f == 0:
            return False
    return True


def prime_factors(n: int) -> Set[int]:
    factors = set()
    f = 2
    while n > 1:
        while n % f == 0:
            factors.add(f)
            n //= f
        f += 1
    return factors


def all_factors(n: int) -> Set[int]:
    factors = {1, n}
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
        i += 1
    return factors


def primes_up_to(n: int) -> Set[int]:
    primes = list(range(2, n + 1))
    x = 0
    while x < len(primes):
        primes = primes[:x + 1] + [i for i in primes[x + 1:] if i % primes[x] != 0]
        x += 1
    return set(primes)


# Strings

def middle_letter(text: str) -> str:
    x = len(text)
    if x % 2 == 0:  # if x is even
        return text[x // 2] + text[(x + 1) // 2]
    else:
        return text[x // 2]


def is_palindrome(word: str) -> bool:
    for i in range(len(word)):
        if word[i] != word[-(1 + i)]:
            return False
    return True


def word_count(text: str) -> Dict[str, int]:
    words = {}
    for word in text.split(" "):
        words[word.lower()] = 1 + words.get(word.lower(), 0)
    return words


# Operations

def mapper(li: list, func) -> list:
    new = []
    for x in li:
        new.append(func(x))
    return new


def reducer(li: list, func):
    if len(li) == 0:
        return None
    if len(li) == 1:
        return li[0]
    result = func(li[0], li[1])
    for x in li[2:]:
        result = func(result, x)
    return result
