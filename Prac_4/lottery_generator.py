def main():
    import random

    no_quick_picks = int(input("How many quick picks? "))
    lottery_numbers = []
    counter = 0
    counter_1 = 0

    while counter_1 != no_quick_picks:

        while counter != 6:
            number = random.randint(1, 45)

            if number not in lottery_numbers:
                lottery_numbers.append(number)
                lottery_numbers.sort()
            else:
                counter -= 1

            counter += 1

        print(lottery_numbers)
        counter = 0
        lottery_numbers = []
        counter_1 += 1


main()
