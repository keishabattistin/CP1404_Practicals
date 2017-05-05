from Prac_8.Car import Taxi
from Prac_8.Car import SilverServiceTaxi

print("Let's drive!")
print('q)uit, c)hoose, d)rive')
choice = input('>>>')
taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Huma', 200, 4)]
count = 0
total_price = 0
selection = ''

while choice != 'q':

    if choice == 'c':
        print('Taxis available:')
        for car in taxis:
            print('{} - {}'.format(count, car))
            count += 1
        count = 0

        taxi_choice = int(input('Choose taxi:'))
        selection = taxis[taxi_choice]

        print('Bill to date: ${:.2f}'.format(total_price))
        print('q)uit, c)hoose, d)rive')
        choice = input('>>>')

    elif choice == 'd':
        distance = int(input('Drive how far? '))
        drive = taxis[taxi_choice].drive(distance)
        fare = taxis[taxi_choice].get_fare()
        total_price += fare
        print('Your {} trip cost you ${}'.format(taxis[taxi_choice].name, fare))
        print('Bill to date: ${:.2f}'.format(total_price))

        print('q)uit, c)hoose, d)rive')
        choice = input('>>>')

    else:
        print('Invalid Input')

    print('Total trip cost: ${}'.format(total_price))
    print('Taxis are now:')
    for car in taxis:
        print('{} - {}'.format(count, car))
        count += 1
