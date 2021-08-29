def check_value(number_1, number_2, var_name):
    in_min = min(float(number_1), float(number_2))
    in_max = max(float(number_1), float(number_2))
    while True:
        test_val = float(
            input("Enter a value for " + var_name + " between " + str(in_min) + " and " + str(in_max) + ":"))
        if in_min <= test_val <= in_max:
            return test_val
        else:
            print("Invalid entry.")


def main():
    period = check_value(5, 10, "period")
    interest_rate = check_value(0.01, 0.05, "interest")
    principal = check_value(10, 100000, "principal")
    total_amt = principal * (1 + interest_rate * period)
    print("The total amount is : " + str(total_amt))


main()
