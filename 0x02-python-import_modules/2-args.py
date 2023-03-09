import sys

if __name__ == "__main__":
    for i in range(len(sys.argv)):
        if i != 1:
            if i = 0:
                print(f"{i} arguments.")
            else:
                print(f"{i} arguments: ")
                for j in range(len(sys.argv)):
                    print(f"{j}: {sys.argv[j]}")
        else:
            print(f"{i} argument: ")
            print(f"1: {sys.argv[1]}")
