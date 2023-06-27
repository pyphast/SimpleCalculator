from CalcFirstNumber import calc_first_number_input
from CalcOperator import calc_operator_input
from CalcSecondNumber import calc_second_number_input
from CalcCalculation import calc_calculation
from CalcRestart import calc_restart


# main program running the calculator
def main():
    while True:

        calc_first_number = calc_first_number_input()
        calc_operator = calc_operator_input()
        calc_second_number = None

        if calc_operator != "*/":
            calc_second_number = calc_second_number_input()

        calc_result = calc_calculation(calc_first_number, calc_operator, calc_second_number)

        if calc_result.is_integer():
            print(f"The result is: {int(calc_result)}")
        else:
            print(f"The result is: {calc_result}")

        calc_restarter = calc_restart()

        if calc_restarter:
            continue
        else:
            print("Closing the calculator...")
            break


if __name__ == "__main__":
    main()
