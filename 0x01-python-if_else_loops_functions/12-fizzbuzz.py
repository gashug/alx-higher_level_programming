def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0: # single out number divisible by 3 only
            print("Fizz ", end="")
        elif i % 5 == 0 and i % 3 != 0: # single out number divisible by 5 only
            print("Buzz ", end="")
        elif i % 3 == 0 and i % 5 == 0: # condition set to catch numbers divisible by both 3 and 5
            print('FizzBuzz ', end="")
        else:
            print(f'{i} ', end="")
