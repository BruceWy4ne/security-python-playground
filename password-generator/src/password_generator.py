import random
import string


def welcome():
    print("="*40)
    print((" "*5)+"Secure Password Generator v1.0"+(" "*5))
    print("="*40)


def passlen():
    try:
        n = int(input("Enter length of password: "))
        return n
    except:
        return 0


def CheckValidation(s):
    n = (input("Include "+s+" (Y/N):")).lower()
    while n != "n" and n != "y":
        print("Please type 'Y' for yes or 'N' for no")
        n = (input("Include "+s+" (Y/N):")).lower()
    return n


def passtype(n):
    i = 0
    while i == 0:
        upperL = CheckValidation("Uppercase Letter")
        lowerL = CheckValidation("Lowercase Letter")
        numbers = CheckValidation("Numbers")
        spc = CheckValidation("Special Character")
        if upperL == "n" and lowerL == "n" and numbers == "n" and spc == "n":
            print("Error: At least one character type must be selected.")
            i = 0
        else:
            i = 1

    genpass(upperL, lowerL, numbers, spc, n)


def genpass(a, b, c, d, l):
    password = ""
    x = len(password)
    ca = 0
    cb = 0
    cc = 0
    cd = 0
    while x < l:

        allowed_char = ""

        if a == "y":
            if ca == 0:
                password += random.choice(string.ascii_uppercase)
                x = len(password)
                ca = 1
            else:
                allowed_char += random.choice(string.ascii_uppercase)

        if x == l:
            break

        if b == "y":
            if cb == 0:
                password += random.choice(string.ascii_lowercase)
                x = len(password)
                cb = 1
            else:
                allowed_char += random.choice(string.ascii_lowercase)

        if x == l:
            break

        if c == "y":
            if cc == 0:
                password += random.choice(string.digits)
                x = len(password)
                cc = 1
            else:
                allowed_char += random.choice(string.digits)

        if x == l:
            break

        if d == "y":
            if cd == 0:
                password += random.choice(string.punctuation)
                x = len(password)
                cd = 1
            else:
                allowed_char += random.choice(string.punctuation)

        if x == l:
            break

        if allowed_char != "":
            password += random.choice(allowed_char)
            x = len(password)
    print("".join(random.sample(password, len(password))))


def main():
    welcome()
    length = passlen()
    if length != 0:
        passtype(length)
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
