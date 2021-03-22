#   Author: Luis Márquez
#   Date: 2021/01/21
#   Description:
#       This is a simple program in which the "Bubble Sort" algorithm is implemented in Python.
#       
#       The user enters a number serie and then, this algorithm, is in charge of ordering in a
#       increasing or decreasing way the numbers, depending on what the user wants.
# #


def bubble_sort_increasing_way(numbers):
    length = numbers.__len__()
    for i in range(1, length):
        for j in range(0, length-i):
            if numbers[j] > numbers[j+1]:
                aux = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = aux


def bubble_sort_decreasing_way(numbers):
    length = numbers.__len__()
    for i in range(1, length):
        for j in range(0, length-i):
            if numbers[j] < numbers[j+1]:
                aux = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = aux


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
    option = True
    print("Welcome to the program...")
    while option:
        print("Press %d to add a number to the list" % 1)
        print("Press %d to print the list" % 2)
        print("Press %d to apply the Bubble Sort in increasing way" % 3)
        print("Press %d to apply the Bubble Sort in decreasing way" % 4)
        print("Press %d to exit" % 0)
        opc = int(input("Type your option here:"))
        if opc == 0:
            print("Bye!")
            exit()
        elif opc == 1:
            add_to_list(numbers)
            print("The numbers were added to the list...")
        elif opc == 2:
            print("The numbers added to the list are:")
            print_list(numbers)
        elif opc == 3:
            print("The list before the sort...")
            print_list(numbers)
            bubble_sort_increasing_way(numbers)
            print("The list after the sort...")
            print_list(numbers)
        elif opc == 4:
            print("The list before the sort...")
            print_list(numbers)
            bubble_sort_decreasing_way(numbers)
            print("The list after the sort...")
            print_list(numbers)

    pause()


if __name__ == "__main__":
    run()