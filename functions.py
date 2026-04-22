def check(a):
    if a % 3 == 0 and a % 5 == 0:
        return "FizzBuzz"
    elif a % 3 == 0:
        return "Fizz"
    elif a % 5 == 0:
        return "Buzz"
    else:
        return str(a)
i = int(input("Write a number"))
for num in range(1, i + 1):
    print(check(num)) 