# """Build a python function that does the following"""
# Accepts: 2 integers
# returns the lowest common multiple of those integers (integer)

# def myfun(a, b):
#     a = int(input("First number:\n"))
#     b = int(input("Second number:\n"))

#     if a > b:
#         greater = a
#     else:
#         greater = b
#     i = 2
#     while (greater%a==0) and (greater%b==0):
#             lcm = greater * i
#             i += 1
#     return lcm

def myfun(x, y):
    """Return the integer LCM of two integer values."""
    if x == 0 or y == 0:
        print("One of the integers is zero")
        return
    start = max(x, y)

    while start % x != 0 or start % y != 0:
        start += max(x, y)
        pass
    return abs(start)


print(myfun(14, 25))
