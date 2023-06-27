from math import sqrt


# takes inputs and calculate them based on operator input
def calc_calculation(enter_first_number, enter_operator, enter_second_number):
    if enter_operator == "+":
        return enter_first_number + enter_second_number
    elif enter_operator == "-":
        return enter_first_number - enter_second_number
    elif enter_operator == "*":
        return enter_first_number * enter_second_number
    elif enter_operator == "/":
        return enter_first_number / enter_second_number
    elif enter_operator == "*/":
        return sqrt(enter_first_number)
    elif enter_operator == "**":
        return enter_first_number ** enter_second_number
