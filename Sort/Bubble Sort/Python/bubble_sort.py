#   Author: Luis Márquez
#   Date: 2021/01/21
#   Description:
#       This is a simple program in which the "Bubble Sort" algorithm is implemented in Python.
#       
#       The user enters a number serie and then, this algorithm, is in charge of ordering in a
#       increasing or decreasing way the numbers, depending on what the user wants.
# #


def increasing_way():
    pass


def decreasing_way():
    pass


def add_to_list(numbers):
    go_on = True

    while go_on:
        try:
            n = int(input("Type the number you want to add to the list: "))
            numbers.append(n)
        except ValueError:
            print("Yo must to type an int value.\n")

        option = str(input("Do you want to add another number? [y/n]"))

        if option == 'n' or option == 'N':
            print("OKAY")
            go_on = False
        elif option == 'Y' or option == 'y':
            print("NEXT")
            continue
        else:
            print("INVALID OPTION")
            break


def print_list(numbers):
    try:
        i = 0
        if numbers:
            for n in numbers:
                print("numbers[%d] = %d" % (i,n))
                i += 1
        else:
            print("The list is empty.\n")
    except ValueError:
        print("EXCEPTION")


# This function pause the flow of the program
def pause():
    input("Press any key to exit...\n")


def run():
    numbers = []
    add_to_list(numbers)
    print_list(numbers)
    pause()


if __name__ == "__main__":
    run()