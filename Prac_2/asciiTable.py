def main():
    lower = int(input("What is the lower range: "))
    upper = int(input("What is the upper range: "))
    get_number(lower, upper)

def get_number(lower, upper):

    try:
        num = int(input("Enter a number between ({}, {}): ".format(lower, upper)))

        if lower > num > upper:
            print("Please enter a valid number")
            num = int(input("Enter a number between ( {}, {} )".format(lower, upper)))

    except ValueError:
        print("Please enter a valid number")
        num = int(input("Enter a number between ( {}, {} )".format(lower, upper)))

#    letter = input("Enter a Character:")
#    code = ord(letter)
#    print("The ASCII Code for", letter, "is:", code)

    counter = 0

    while counter == 0:

        if lower <= num <= upper:
            print("The Character for", num, "is:", chr(num))
            counter += 1

        else:
            print("Invalid Number")
            num = int(input("Enter a Number Between {} and {}:".format(lower, upper)))

    while lower < upper:
        lower += 1

    display = '{}  {}'.format(lower, chr(lower))

    print(display)

main()
