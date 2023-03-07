def uppercase(str):
    new_string = ""
    for i in str:
        if 97 <= ord(i) <= 122:  # check if character is lowercase
            new_string = new_string + chr(ord(i) - 32)  # subtract 32 from ASCII code and convert back to character
        else:
            new_string = new_string + i  # keep character as it is

    print(new_string)
