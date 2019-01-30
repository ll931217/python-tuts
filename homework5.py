x = 1

def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if not (x % i):
                return False
    else:
        return False
    return True

while x <= 100:
    if isPrime(x):
        print('Prime')
    elif x % 5 == 0 & x % 3 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
    x += 1
