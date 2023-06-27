from CalcNumberHelper import calc_number_helper
from CalcExit import calc_exit


# checks second number input
def calc_second_number_input():
    while True:
        enter_second_number = input("Please enter the second number: ")
        if enter_second_number.lstrip("-").isdigit():
            enter_second_number = float(enter_second_number)
            break
        elif enter_second_number == "help":
            calc_number_helper()
            continue
        elif enter_second_number == "exit":
            calc_exit()
        else:
            print("The input is invalid. "
                  "Please enter a valid number or write 'help' for further support.\n")
            continue

    return enter_second_number
