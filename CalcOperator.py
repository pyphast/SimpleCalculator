from CalcOperatorHelper import calc_operator_helper
from CalcExit import calc_exit


# checks operator input
def calc_operator_input():
    while True:
        operator_signs = ["+", "-", "*", "/", "*/", "**"]
        enter_operator = input("Please enter an operator: ")
        if enter_operator == "help":
            calc_operator_helper()
            continue
        elif enter_operator == "exit":
            calc_exit()
        elif enter_operator not in operator_signs:
            print("The sign is incorrect. Please enter one of the following signs: \n"
                  "+, -, *, /, */, ** or write 'help' for further support.\n")
            continue
        else:
            break

    return enter_operator
