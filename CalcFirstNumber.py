from CalcNumberHelper import calc_number_helper
from CalcExit import calc_exit


# checks first number input
def calc_first_number_input():
    while True:
        enter_first_number = input("Please enter the first number: ")
        if enter_first_number.lstrip("-").isdigit():
            enter_first_number = float(enter_first_number)
            break
        elif enter_first_number == "help":
            calc_number_helper()
            continue
        elif enter_first_number == "exit":
            calc_exit()
        else:
            print("The input is invalid. "
                  "Please enter a valid number or write 'help' for further support.\n")
            continue

    return enter_first_number
