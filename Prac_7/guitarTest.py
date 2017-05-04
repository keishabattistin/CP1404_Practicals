from Prac_7.Guitar import Guitar

def main():
    # no_guitars = input('How many Guitars do you have?')

    print('My guitars!')

    # for guitar in no_guitars:
    name1 = input('Name: ')
    year1 = int(input('Year: '))
    cost1 = float(input('Cost: $'))

    print('{} ({}) : $ {:8,.2f} added'.format(name1, year1, cost1))

    print('...snip...')
    # name2 = input('Name: ')
    # year2 = int(input('Year: '))
    # cost2 = float(input('Cost: $'))
    #
    # print('{} ({}) : $ {:8,.2f} added'.format(name2, year2, cost2))
    #
    # name3 = input('Name: ')
    # year3 = int(input('Year: '))
    # cost3 = float(input('Cost: $'))
    #
    # print('{} ({}) : $ {:8,.2f} added'.format(name3, year3, cost3))

    one = Guitar(name1, year1, cost1)
    two = Guitar('Gibson L-5 CES', 1922, 16035.4)
    three = Guitar('Line6 JTV-59', 2010, 1512.9)

    print(one)
    print(two)
    print(three)

main()