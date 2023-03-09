import sys

if __name__ == "__main__":
    arg_list = sys.argv[1:]
    sum = 0
    for i in arg_list:
        sum += i

    print(sum)
