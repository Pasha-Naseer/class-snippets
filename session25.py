"""
So we are trying to explore the storage difference between
C and Python while formatting numbers; Both languages benefit form
IEEE-754 which is the international standard that defines how
floating point numbers are.
Python float --> double precision (64-bit)
C float --> single precision (32-bit)
C double -->  double precision (64-bit)
Round half-even (Banker’s rounding) is a method which Python and C both use
It means if the digit to be rounded is exactly 5 and nothing follows it,
you round to the nearest even last digit;
Nevertheless most decimal literals aren't exactly half in binary.
When rounding decimal floats in these two languages,
first they are approximated to the nearest binary floats and then rounded,
and true tie in their binary equivalent rarely happens.
"""

# Original code is in my CPROJECTS repo
a = 1234
print(f"{a:2}")
print(f"{a:4}")
print(f"{a:5}")

print("********")

b = 123.43
print(f"{b:5.3f}")
print(f"{b:5.2f}")
print(f"{b:5.1f}")
print(f"{b:6.2f}")
print(f"{b:7.2f}")

print("********")

c = 123.45
print(f"{c:5.3f}")
print(f"{c:5.2f}")
print(f"{c:5.1f}")  # In C it returns 123.4
print(f"{c:6.2f}")
print(f"{c:7.2f}")

print("********")

d = 123.425
print(f"{d:5.2f}")  # In C it returns 123.43

e = 123.424
print(f"{e:5.2f}")

test = 123.435
print(f"{test:5.2f}")  # In C it returns 123.43
