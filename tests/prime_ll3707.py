import math

def is_prime(n):
    """
    This function check if a number is prime.
    
    Parameters
    ----------
    n (int) : The integer input to check.
    
    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    
    Examples
    --------
    >>> is_prime(3)
    True
    >>> is_prime(15)
    False
    """
    if n<= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    