menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[0] Exit

=> """

balance = 0
limit = 500
statement = ""
receipt = ""
withdraw_count = 0
WITHDRAW_LIMIT = 3

while True:
    option = input(menu)

    if option == "1":
        value = float(input("\nEnter the deposit amount: "))

        if value > 0:
            balance += value
            statement += f"\nDeposit of $ {value:.2f}"
            receipt = f"\nDeposit of $ {value:.2f}"
            print(receipt)

        else:
            print("\nOperation failed! The entered value is invalid.")

    elif option == "2":
        value = float(input("\nEnter the withdrawal amount: "))

        exceeded_balance = value > balance
        exceeded_limit = value > limit
        exceeded_withdrawals = withdraw_count >= WITHDRAW_LIMIT

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
            print("\nOperation failed! O valor informado é inválido.")

    elif option == "3":
        print("\n========== STATEMENT ==========")
        print("\nNo transactions have been made." if not statement else statement)
        print("\n...............................")
        print(f"\nBalance: $ {balance:.2f}")
        print("\n===============================")

    elif option == "0":
        break

    else:
        print("\nInvalid option! Please select the desired operation again.")
