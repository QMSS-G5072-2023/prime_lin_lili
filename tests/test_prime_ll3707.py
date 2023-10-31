import prime_ll3707
from prime_ll3707 import is_prime
def test_is_prime():
    assert is_prime(2) == True, "2 should be a prime number"
    assert is_prime(7) == True, "7 should be a prime number"
    assert is_prime(8) == False, "8 should not be a prime number"
    assert is_prime(9) == False, "9 should not be a prime number"