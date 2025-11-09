"""
Problem: Reverse a Number
Difficulty: Easy

"""

def reverse_number(n: int) -> int:
    # TODO: implement correctly handling signs and overflow if needed
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10

        # Overflow detection
        if rev > (INT_MAX - (n % 10)) // 10:
            print("Overflow detected!")
            return 0
        

    return sign * rev

    # Clamp again in case of signed overflow
    if rev < INT_MIN or rev > INT_MAX:
        print("Overflow detected!")
        return 0

if __name__ == "__main__":
    print(reverse_number(12345))
