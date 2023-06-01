#!/usr/bin/python3
"""Prime game module.
"""


def determineWinner(rounds, numbers):
    """Determines the winner of a prime game session with `rounds` rounds.
    """
    if rounds < 1 or not numbers:
        return None
    maria_wins, ben_wins = 0, 0
    # Generate primes with a limit of the maximum number in numbers
    limit = max(numbers)
    primes = [True for _ in range(1, limit + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, limit + 1, i):
            primes[j - 1] = False
    # Filter the number of primes less than limit in numbers for each round
    for _, num in zip(range(rounds), numbers):
        primes_count = len(list(filter(lambda x: x, primes[0: num])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
