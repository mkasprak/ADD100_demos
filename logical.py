"""
    Logical operators
"""

a = 10
b = 5
c = 0

if a > c and b > c:
    print("Both a and b are greater than C")
if a > c or b > c:
    print("Either, or both, a or b is greater than c.")
if c != 0:
    print("c is not equal to 0")
else:
    print("c is equal to 0")
