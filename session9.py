import math
import time

# See if the number is prime


def prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return None
        else:
            return number
    else:
        return None


def prime2(number):
    if number > 1:
        for i in range(2, math.ceil(math.sqrt(number))):
            if number % i == 0:
                return None
        else:
            return number
    else:
        return None


# trying to compare the process time of the two functions
x = time.time()
print(prime2(2345347856234767467425253643234567909876543456789876543456789876543456789876541))
y = time.time()
print(y - x)

x = time.time()
print(prime(2345347856234767467425253643234567909876543456789876543456789876543456789876541))
y = time.time()
print(y - x)
# oh!

def factor(number, primes):
    factor_list = []
    primes_list = primes
    for j in primes_list:
        if number % j == 0:
            factor_list.append(j)
            number = number / j
            primes_list.append(j)
        if number == 1:
            return factor_list
    else:
        factor_list.append(number)
        return factor_list


num = int(input("Enter a number: "))
num2 = int(input("Enter the second number: "))
prime_list = []
for e in range(2, num):
    if prime(e) == e:
        prime_list.append(e)
prime_list2 = []
for a in range(2, num2):
    if prime(a) == a:
        prime_list2.append(a)

first_factor = factor(num, prime_list)
second_factor = factor(num2, prime_list2)
print(first_factor)
print(second_factor)


# Least Common Multiple
def kmm_calculator(first_factor_list, second_factor_list):
    kmm_list = list(set(first_factor_list + second_factor_list))
    final_list = []
    for g in kmm_list:
        first = first_factor_list.count(g)
        second = second_factor_list.count(g)
        if first > second:
            calculation = g ** first
        elif second > first:
            calculation = g ** second
        else:
            calculation = g ** first
        final_list.append(calculation)
    kmm = 1
    for h in final_list:
        kmm *= h
    return kmm


print("Greatest Common Divisor")
print(kmm_calculator(first_factor, second_factor))


# Greatest Common Divisor
def bmm_calculator(first_factor_list, second_factor_list):
    bmm_list = []
    result_list = []

    for b in first_factor_list:
        if b in second_factor_list:
            bmm_list.append(b)
    if bmm_list:
        for c in bmm_list:
            first = first_factor_list.count(c)
            second = second_factor_list.count(c)
            if first < second:
                calculation = c ** first
            elif second < first:
                calculation = c ** second
            else:
                calculation = c ** first
            result_list.append(calculation)
            while c in first_factor:
                first_factor_list.remove(c)
    bmm = 1
    for f in result_list:
        bmm *= f
    return bmm


print("Greatest Common Divisor")
print(bmm_calculator(first_factor, second_factor))


# Euclidean Algorithm (for Greatest Common Divisor)
def euclidean_gcd(number1, number2):
    while True:
        x = number1 % number2
        if x == 0:
            return number2
        number1 = number2
        number2 = x


print("Greatest Common Divisor")
print(euclidean_gcd(num, num2))
