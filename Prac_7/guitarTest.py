from Prac_7.Guitar import Guitar

def main():
    no_guitars = input('How many Guitars do you have?')

    print('My guitars!')
    list = []

    for guitar in no_guitars:
        name = input('Name: ')
        year = int(input('Year: '))
        cost = float(input('Cost: $'))
        print('{} ({}) : ${}.added')


    # one = Guitar('Fender Stratocaster', 2014, 765.40)
    # two = Guitar('Gibson L-5 CES', 1922, 16035.40)
    # three = Guitar('Line 6 JTV-59', 2010, 1512.90)

    print(one)
    print(two)
    print(three)

main()