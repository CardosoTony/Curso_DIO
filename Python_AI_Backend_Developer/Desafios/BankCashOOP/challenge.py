import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def perform_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)


class Individual(Client):
    def __init__(self, name, date_of_birth, cpf, address):
        super().__init__(address)
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf


class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, amount):
        balance = self.balance
        exceeded_balance = amount > balance

        if exceeded_balance:
            print("\n=== Operation failed! You don't have sufficient balance. ===")

        elif amount > 0:
            self._balance -= amount
            print("\n=== Withdrawal successful! ===")
            return True

        else:
            print("\n=== Operation failed! The amount entered is invalid. ===")

        return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("\n=== Deposit successful! ===")
        else:
            print("\n=== Operation failed! The amount entered is invalid. ===")
            return False

        return True


class CheckingAccount(Account):
    def __init__(self, number, client, limit=500, withdrawal_limit=3):
        super().__init__(number, client)
        self._limit = limit
        self._withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        number_of_withdrawals = len(
            [transaction for transaction in self.history.transactions if transaction["type"]
                == Withdrawal.__name__]
        )

        exceeded_limit = amount > self._limit
        exceeded_withdrawals = number_of_withdrawals >= self._withdrawal_limit

        if exceeded_limit:
            print("\n=== Operation failed! You don't have sufficient balance. ===")

        elif exceeded_withdrawals:
            print(
                "\n=== Operation failed! You have exceeded the maximum number of withdrawals. ===")

        else:
            return super().withdraw(amount)

        return False

    def __str__(self):
        return f"""
            Agency:\t{self.agency}
            C/C:\t{self.number}
            Holder:\t{self.client.name}
        """


class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "amount": transaction.amount,
            }
        )


class Transaction(ABC):
    @property
    @abstractproperty
    def amount(self):
        pass

    @abstractclassmethod
    def register(self, account):
        pass


class Withdrawal(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account):
        transaction_success = account.withdraw(self.amount)

        if transaction_success:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account):
        transaction_success = account.deposit(self.amount)

        if transaction_success:
            account.history.add_transaction(self)


def menu():
    menu = """\n
    ================= MENU =================

    [1] Deposit
    [2] Withdraw
    [3] Statement
    [4] New user
    [5] New account
    [6] List accounts
    [0] Exit

    => """
    return input(textwrap.dedent(menu))


def filter_client(cpf, clients):
    filtered_clients = [client for client in clients if client.cpf == cpf]
    return filtered_clients[0] if filtered_clients else None


def get_client_account(client):
    if not client.accounts:
        print("\n=== Client does not have an account! ===")
        return

    # FIXME: Does not allow client to choose account
    return client.accounts[0]


def deposit(clients):
    cpf = input("Enter client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n=== Client not found! ===")
        return

    amount = float(input("Enter deposit amount: "))
    transaction = Deposit(amount)

    account = get_client_account(client)
    if not account:
        return

    client.perform_transaction(account, transaction)


def withdraw(clients):
    cpf = input("Enter client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n=== Client not found! ===")
        return

    amount = float(input("Enter withdrawal amount: "))
    transaction = Withdrawal(amount)

    account = get_client_account(client)
    if not account:
        return

    client.perform_transaction(account, transaction)


def show_statement(clients):
    cpf = input("Enter client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n=== Client not found! ===")
        return

    account = get_client_account(client)
    if not account:
        return

    print("\n=============== STATEMENT ==============")
    transactions = account.history.transactions

    statement = ""
    if not transactions:
        statement = "No transactions have been made."
    else:
        for transaction in transactions:
            statement += f"\n{transaction['type']
                              }:\t$ {transaction['amount']:.2f}"

    print(statement)
    print(f"\nBalance:\t$ {account.balance:.2f}\n")
    print("=" * 40)


def create_client(clients):
    cpf = input("Enter CPF (numbers only): ")
    client = filter_client(cpf, clients)

    if client:
        print("\n=== Client with this CPF already exists! ===")
        return

    name = input("Enter full name: ")
    date_of_birth = input("Enter date of birth (dd-mm-yyyy): ")
    address = input(
        "Enter address (street, number - neighborhood - city/state): ")

    client = Individual(
        name=name, date_of_birth=date_of_birth, cpf=cpf, address=address)

    clients.append(client)

    print("\n=== Client created successfully! ===")


def create_account(account_number, clients, accounts):
    cpf = input("Enter client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n=== Client not found, account creation flow terminated! ===")
        return

    account = CheckingAccount.new_account(client=client, number=account_number)
    accounts.append(account)
    client.accounts.append(account)

    print("\n=== Account created successfully! ===")


def list_accounts(accounts):
    if not accounts:
        print("\n=== There are no accounts! ===")
        return

    print("\n=========== LIST OF ACCOUNTS ===========")

    for account in accounts:
        print(textwrap.dedent(str(account)))

    print("=" * 40)


def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == "1":
            deposit(clients)

        elif option == "2":
            withdraw(clients)

        elif option == "3":
            show_statement(clients)

        elif option == "4":
            create_client(clients)

        elif option == "5":
            account_number = len(accounts) + 1
            create_account(account_number, clients, accounts)

        elif option == "6":
            list_accounts(accounts)

        elif option == "0":
            break

        else:
            print(
                "\n=== Invalid operation, please select the desired operation again. ===")


main()
