# checks if restart of calculation is wanted
def calc_restart():
    while True:
        enter_restart = input("Do you want to restart the calculation? "
                              "Please enter 'Y' or 'y' for yes and 'N' or 'n' for no: ")
        if enter_restart == "Y" or enter_restart == "y":
            return True
        elif enter_restart == "N" or enter_restart == "n":
            return False
        else:
            print("The input is invalid. "
                  "Please enter 'Y' or 'y' for yes and 'N' or 'n' for no.\n")
            continue
