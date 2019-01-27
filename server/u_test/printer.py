import sys, os, datetime, re
from .models import Account, Customer, Statement
from typing import List



class Printer:
    "A class to print accounts, customers, and statements."

    tab_size = 4

    def __init__(self, accounts: List[Account], customers: List[Customer]) -> None:
        """Iterate over and print accounts, customers, and statements."""
        self.print_header()
        self.print_account_header(len(accounts))
        for account in accounts:
            self.print_account(account)
            self.print_customer_header(len(customers))
            for customer in customers:
                self.print_customer(customer)
            self.print_statement_header(len(account.statements))
            # sort statements by date
            statements = sorted(account.statements, key=lambda s: s.date, reverse=True)
            # remove currency symbols and convert to numbers
            for statement in statements:
                statement.amount = float(re.sub("[^0-9.]", "", statement.amount))
                statement.balance = float(re.sub("[^0-9.]", "", statement.balance))
            # add negative sign if account balance decreased
            for i in range(0, len(statements)):
                if (i+1 < len(statements) and statements[i].balance < statements[i+1].balance):
                    statements[i].amount = -1 * statements[i].amount
            for statement in statements:
                self.print_statement(statement)
            self.print_empty_row()

    def tab(self, number_of_tabs: int) -> str:
        """Return tabs as spaces."""
        return ' ' * (number_of_tabs * self.tab_size)

    def print_empty_row(self) -> None:
        """Prints an empty row."""
        sys.stdout.buffer.write((os.linesep).encode('utf-8'))

    def print_header(self) -> None:
        """Prints the global header."""
        self.print_empty_row()
        sys.stdout.buffer.write(('# Resultado Ex:'+os.linesep).encode('utf-8'))
        sys.stdout.flush()

    def print_account_header(self, size: int) -> None:
        """Prints the account header with number of accounts."""
        sys.stdout.buffer.write(('Accounts ( ' + str(size) + ' )' + os.linesep).encode('utf-8'))
        sys.stdout.flush()

    def print_account(self, account: Account) -> None:
        """Prints an individual account object."""
        sys.stdout.buffer.write((self.tab(1) + 'Account Data:' + os.linesep).encode('utf-8'))
        sys.stdout.buffer.write(str(account).expandtabs(self.tab_size).encode('utf-8'))
        self.print_empty_row()
        sys.stdout.flush()

    def print_customer_header(self, size: int) -> None:
        """Prints the customer header with number of customers"""
        sys.stdout.buffer.write((self.tab(1) + 'Total customers: ' + str(size) + os.linesep).encode('utf-8'))
        sys.stdout.flush()

    def print_customer(self, customer: Customer) -> None:
        """Prints an individual customer object."""
        sys.stdout.buffer.write((self.tab(2) + 'Customer Data:' + os.linesep).encode('utf-8'))
        sys.stdout.buffer.write(str(customer).expandtabs(self.tab_size).encode('utf-8'))
        self.print_empty_row()
        sys.stdout.flush()

    def print_statement_header(self, size: int) -> None:
        """Prints the statement header with number of statements."""
        sys.stdout.buffer.write((self.tab(1) + 'Statements ( ' + str(size) + ' )' + os.linesep).encode('utf-8'))
        sys.stdout.buffer.write((self.tab(2) + 'Date       | Amount | Balance | Concept' + os.linesep).encode('utf-8'))
        sys.stdout.flush()

    def print_statement(self, statement: Statement) -> None:
        """Prints an individual statement object."""
        sys.stdout.buffer.write(str(statement).expandtabs(self.tab_size).encode('utf-8'))
