n=int(input("Введите число: "))

def fizz_buzz(n):
    for m in range(1, n+ 1):
        if m % 3==0 and m % 5==0:
            print("FizzBuzz")
        elif  m % 5==0:
            print("Buzz")
        elif m % 3==0:
            print("Fizz")
        else:
            print(m)
fizz_buzz(n)
