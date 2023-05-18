#!/usr/bin/python3
"""Module for determining the minimum number of coins required to reach a given total amount
"""


def make_change(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    remaining_total = total
    coin_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remaining_total > 0:
        if coin_idx >= n:
            return -1
        if remaining_total - sorted_coins[coin_idx] >= 0:
            remaining_total -= sorted_coins[coin_idx]
            coin_count += 1
        else:
            coin_idx += 1
    return coin_count
