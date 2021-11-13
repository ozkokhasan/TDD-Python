def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(value, 5):
        return "Buzz"
    return str(value)

def isMultiple(value, mod):
    return (value % mod) == 0

def check_fizzBuzz(value, expectedValue):
    value = fizzBuzz(value)
    assert value == expectedValue

def test_returns_1_with_1_PassedIn():
    check_fizzBuzz(1, "1")

def test_returns_2_with_2_PassedIn():
    check_fizzBuzz(2, "2")

def test_returns_Fizz_with_3_PassedIn():
    check_fizzBuzz(3, "Fizz")

def test_returns_Buzz_with_5_PassedIn():
    check_fizzBuzz(5, "Buzz")

def test_returns_Fizz_with_6_PassedIn():
    check_fizzBuzz(6, "Fizz")

def test_return_Buzz_with_10_PassedIn():
    check_fizzBuzz(10, "Buzz")

def test_returns_FizzBuzz_with_15_PassedIn():
    check_fizzBuzz(15, "FizzBuzz")
