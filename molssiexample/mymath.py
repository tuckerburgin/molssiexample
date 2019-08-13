"""
A file for executing math functions.
"""
import random
import math


def fact(x):
    tot = x
    if x == 0:
        return 1
    for i in range(x):
        if i > 0:
            tot = tot * i
    return tot


def euler(n=10):
    """
    Evaluate Taylor expansion of Euler number :math:`e` to n terms.

    .. math::

        e = \\sum_{x=0}^n \\frac{1}{x!}

    Parameters
    ----------
    n : int, Optional, default: 10
        Number or terms in taylor expansion; must be >= 0

    Returns
    -------
    sum : float
        Resulting approximation of Euler number

    """

    if n < 0:
        raise ValueError("n must be >= 0")
    sum = 0
    for i in range(n + 1):
        sum += 1**i / fact(i)
    return sum


def pi(n=100):
    """
    Approximate pi using stochastic method with n iterations.

    Parameters
    ----------
    n : int, Optional, default: 100
        Number or iterations in stochastic method; must be >= 0

    Returns
    -------
    sum : float
        Resulting approximation of pi
    """

    count = 0
    for i in range(n):
        if math.sqrt(random.random()**2 + random.random()**2) < 1:
            count += 1
    ratio = count / n  # ratio of in circle to outside circle
    pi = ratio * 4
    return (pi)


