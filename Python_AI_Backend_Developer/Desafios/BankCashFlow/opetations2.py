import textwrap


def menu():
    menu = """

    [1] Deposit
    [2] Withdraw
    [3] Statement
    [4] New account
    [5] New user
    [6] List accounts
    [0] Exit

    => """
    return input(menu)


def deposit(value, balance, statement, /):
    if value > 0:
        balance += value
        statement += f"\nDeposit of $ {value:.2f}"
        receipt = f"\nDeposit of $ {value:.2f}"
        print(receipt)

    else:
        print("\nOperation failed! The entered value is invalid.")

    return value, statement


def withdraw(*, balance, value, statement, limit, withdraw_count, withdraw_limit):

    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = withdraw_count >= withdraw_limit

    if exceeded_balance:
        print(
            "\nOperation failed! You do not have sufficient balance for withdrawal.")

    elif exceeded_limit:
        print("\nOperation failed! You have exceeded the withdrawal limit.")

    elif exceeded_withdrawals:
        print(
            "\nOperation failed! You have already exceeded the daily withdrawal limit.")

    elif value > 0:
        balance -= value
        statement += f"\nWithdrawal of $ {value:.2f}"
        withdraw_count += 1
        receipt = f"\nWithdrawal of $ {value:.2f}"
        print(receipt)

    else:
        print("\nOperation failed! The entered value is invalid.")

    return balance, statement, withdraw_count


def statement_print(balance, /, *, statement):
    print("\n========== STATEMENT ==========")
    print("\nNo transactions have been made." if not statement else statement)
    print("\n...............................")
    print(f"\nBalance: $ {balance:.2f}")
    print("\n===============================")


def create_account(branch, account_number, users):
    cpf = input("\nPlease enter the user's CPF: ")
    user = filter_user(cpf, users)

    if user:
        print("\n===== Account created successfully! =====")
        return {"branch": branch, "account_number": account_number, "user": user}

    print("\n===== User not found! Account creation process terminated. =====")


def create_user(users):
    cpf = input("\nPlease enter the CPF (numbers only): ")
    user = filter_user(cpf, users)

    if user:
        print("\nA user with this CPF already exists!")
        return

    name = input("Please enter the full name: ")
    date_of_birth = input("Please enter the date of birth (dd-mm-yyyy): ")
    address = input(
        "Please enter the address (street, number - neighborhood - city/state abbreviation): ")

    users.append({"name": name, "date_of_birth": date_of_birth,
                 "cpf": cpf, "address": address})
    print("\n===== User created successfully! =====")


def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None


def list_account(accounts):
    print("\n========== Accounts ==========")

    for account in accounts:
        line = f"""
            Branch:\t{account['branch']}
            C/C:\t{account['account_number']}
            Holder:\t{account['user']['name']}
        """
        print(textwrap.dedent(line))

    print("=" * 30)


def main():
    balance = 0
    limit = 500
    statement = ""
    withdraw_count = 0
    users = []
    accounts = []
    account_number = 1
    WITHDRAW_LIMIT = 3
    BRANCH = "0001"

    while True:
        option = menu()

        if option == "1":
            value = float(input("\nEnter the deposit amount: "))

            balance, statement = deposit(value, balance, statement)

        elif option == "2":
            value = float(input("\nEnter the withdrawal amount: "))

            balance, statement, withdraw_count = withdraw(
                balance=balance,
                value=value,
                statement=statement,
                limit=limit,
                withdraw_count=withdraw_count,
                withdraw_limit=WITHDRAW_LIMIT,
            )

        elif option == "3":
            statement_print(balance, statement=statement)

        elif option == "4":
            account = create_account(BRANCH, account_number, users)

            if account:
                accounts.append(account)
                account_number += 1

        elif option == "5":
            create_user(users)

        elif option == "6":
            list_account(accounts)

        elif option == "0":
            break

        else:
            print("\nInvalid option! Please select the desired operation again.")


main()
