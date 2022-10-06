"""
Egyptian algorithm
"""

def egyptian_multiplication(a, n):
    """
    returns the product a * n

    assume n is a nonegative integer
    """
    def isodd(n):
        """
        returns True if n is odd
        """
        return n & 0x1 == 1
    if n < 0:
        print("Error: n should be nonegative")
    if type(n) != int:
        print("Error: n should be an integer")
    else:
        if n == 1:
            return a
        if n == 0:
            return 0
        elif isodd(n):
            return egyptian_multiplication(a + a, n // 2) + a
        else:
            return egyptian_multiplication(a + a, n // 2)

# previous version:
# def power(a, n):
#     """
#     computes the power a ** n
    
#     assume n is a nonegative integer
#     """
#     i = 1; x = a
#     while i < n:
#         x = egyptian_multiplication(x, a)
#         i += 1
#     return x

def power(a,n):
    def isodd(n):
        """
        returns True if n is odd
        """
        return n & 0x1 == 1
    if n == 1:
        return a
    if n == 0:
        return 1
    if isodd(n):
        return power(a * a, n // 2) * a
    else:
        return power(a * a, n // 2)
    

if __name__ == '__main__':
    # this code runs when executed as a script
    print("{} ** {} = {}".format(3, 3, power(3,3)))
    print("{} ** {} = {}".format(4, 4, power(4,4)))
    print("{} ** {} = {}".format(5, 3, power(5,3)))
