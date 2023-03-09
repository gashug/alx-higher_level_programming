#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    result_1 = add(a, b)
    result_2 = sub(a, b)
    result_3 = mul(a, b)
    result_4 = div(a, b)

    print(f"{a} + {b} = {result_1}")
    print(f"{a} - {b} = {result_2}")
    print(f"{a} * {b} = {result_3}")
    print(f"{a} / {b} = {result_4}")
