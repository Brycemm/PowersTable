# dunder
if __name__ == "__main__":
    keep_running = True
    while keep_running:

        number = int(input("Enter an integer: "))
        # adding table format
        print(f'{"Number":>6}\t{"Square":>8}\t{"Cube":>6}')

        # range inclusive of user input
        for num in range(1, number + 1):
            square = num ** 2
            cube = num ** 3
            print(f'{num:>6}\t{square:>8}\t{cube:>6}')
            # user input for loop
        response = input("Would you like to continue? Y/N ")
        if response == "Y":
            keep_running = True
        elif response == "N":
            keep_running = False
