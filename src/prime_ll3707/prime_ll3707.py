import math

def is_prime(n):
    """This function check if a number is prime.
    Parameter:
    - n (int): The integer input to check.
    Return:
    - bool: True if the input integer is a prime number, False otherwise.
    Examples:
    ```python
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
    