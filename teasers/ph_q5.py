import pandas as pd

pd.options.mode.chained_assignment = None  # this is to suppress warnings from pandas when updating chained dataframe


def read_employee_data():
    df = pd.read_csv("employee_details.csv")
    return df


def load_expense_records():
    df = pd.read_csv("expense_records.csv", engine="python", quotechar='"')
    return df


def login(employee_data):
    current_user = None
    while current_user is None:
        user_name = input("Please enter user ID: ")
        user_pwd = input("Enter password: ")
        result = employee_data.loc[lambda df: (df['login_password'] == user_pwd) & (df['employee_id'] == user_name), :]
        if len(result) > 0:
            current_user = result.iloc[0]
            return current_user
        else:
            print("Wrong credentials. Please try again.\n")


def display_menu(current_user):
    choice = None
    while choice is None:
        valid_choices = ["1", "2", "e"]
        print("\n\nSelect the options below:")
        print("[1] Update expense record")
        print("[2] Retrieve personal records")
        if current_user['position'] == "Manager":
            print("[3] Verify submitted records")
            print("[4] Retrieve department data")
            print("[5] Get company data")
            valid_choices.extend(["3", "4", "5"])
        print("[e] Exit")
        choice = input("Choice: ")
        if choice not in valid_choices:
            choice = None

    return choice


def homepage(current_user, employee_data, expense_data):
    has_made_changes = False
    while True:
        user_choice = display_menu(current_user)
        print(f"Your choice is [{user_choice}].")
        if user_choice == "e":
            save_all_data(current_user, expense_data, has_made_changes)
            print("Bye!")
            exit()
        elif user_choice == '1':
            save_all_data(current_user, expense_data, has_made_changes)
        elif user_choice == '2':
            show_personal_data(current_user)
        elif user_choice == "3":
            expense_data, has_made_changes = verify_expense(current_user, expense_data, has_made_changes)
        elif user_choice == '4':
            show_not_implemented()
        elif user_choice == '5':
            show_not_implemented()


def show_personal_data(current_user):
    print("\n\nHere are your personal information:")
    print(f"Employee ID: {current_user['employee_id']}")
    print(f"Name: {current_user['employee_name']}")
    print(f"Position: {current_user['position']}")
    print(f"Department: {current_user['department']}")
    # show more information if there is a need


def show_not_implemented():
    print("[WARNING] This function has not been implemented. Look out for next change!")


def save_all_data(current_user, expense_data, has_made_changes):
    if has_made_changes and current_user['position'] == "Manager":
        print("Detected changes to expense data. Saving now...")
        expense_data.to_csv("expense_records.new.csv", index=False, quotechar='"')
    elif current_user['position'] == "Manager":
        print("No changes were made on expense data during session. Ignore request.")
    # WARNING: The above does not always double quote the amount spent but only when it has
    # the thousands comma which is different from original format


def verify_expense(current_user, expense_data, has_made_changes):
    # defense programming: need to ensure this is a manager before we proceed
    if current_user['position'] == "Manager" and expense_data is not None:
        available_df = expense_data[
            (expense_data['status'] == 'Pending') & (expense_data['department'] == current_user['department'])]
        # We only show expense records which are pending approval and those belonging to the department of the manager
        # Should not allow approval of expenses which are belonging to another department!

        for i, row in available_df.iterrows():
            print(f"Employee ID: {available_df.employee_id[i]}")
            print(f"Employee Name: {available_df.employee_name[i]}")
            print(f"Amount spent: {available_df.amount_spent[i]}")
            print(f"Status: {available_df.status[i]}")
            print(f"Date of spending: {available_df.spending_date[i]}")
            action = None
            while action is None:
                action = input("[A]pprove, [D]eny, [S]kip?: ")
                action = action.lower()
                if action == 'a':
                    if available_df.status[i] != "Approved":
                        has_made_changes = True
                        available_df.status[i] = "Approved"
                elif action == 'd':
                    if available_df.status[i] != "Deny":
                        has_made_changes = True
                        available_df.status[i] = "Deny"
                elif action == 's':
                    continue
        expense_data.update(available_df)
    return expense_data, has_made_changes


def main():
    employee_data = read_employee_data()
    current_user = login(employee_data)
    expense_data = load_expense_records()
    homepage(current_user, employee_data, expense_data)


if __name__ == "__main__":
    main()
