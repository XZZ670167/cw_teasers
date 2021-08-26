def check_value(number_1, number_2, var_name):
    in_min = min(float(number_1), float(number_2))
    in_max = max(float(number_1), float(number_2))
    while True:
        test_val = float(
            input("Enter a value for " + var_name + " between " + str(in_min) + " and " + str(in_max) + ":"))
        if in_min <= test_val <= in_max:
            print("Value of " + str(test_val) + " is accepted.")
            break
        else:
            print("Invalid entry.")


check_value(10, 100, 'principal')
