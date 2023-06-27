from CalcFirstNumber import calc_first_number_input
from CalcOperator import calc_operator_input
from CalcSecondNumber import calc_second_number_input
from CalcCalculation import calc_calculation
from CalcRestart import calc_restart


# main program running the calculator
def main():
    while True:
        # run the input functions
        calc_first_number = calc_first_number_input()
        calc_operator = calc_operator_input()
        calc_second_number = None

        # only run second number input if user doesn't want to have the square root of first number
        if calc_operator != "*/":
            calc_second_number = calc_second_number_input()

        # calculate the inputs
        calc_result = calc_calculation(calc_first_number, calc_operator, calc_second_number)

        # check if calculation result is a whole number
        if calc_result.is_integer():
            print(f"The result is: {int(calc_result)}")
        else:
            print(f"The result is: {calc_result}")

        # run calculator restart function
        calc_restarter = calc_restart()

        # check status of calculator restart function
        if calc_restarter:
            continue
        else:
            print("Closing the calculator...")
            break


if __name__ == "__main__":
    main()
