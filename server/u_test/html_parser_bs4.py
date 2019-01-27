import sys
from bs4 import BeautifulSoup
from .models import Customer, Account, Statement
from typing import List



class HtmlParserBs4:
    """A class used to parse html to objects."""

    def __init__(self) -> None:
        pass

    def parse_customers_html_to_objects(self, customers_html: str, username: str) -> List[Customer]:
        """Iterate over the customers' html, and create and return Customer objects."""
        customers = list()
        soup = BeautifulSoup(customers_html, 'html.parser')
        custs = soup.find_all('ul', attrs={'class':'collection with-header'})
        for cust in custs:
            attributes = cust.find_all('li')
            name = ''
            address = ''
            emails = ''
            phones = ''
            i = 0
            for attribute in attributes:
                if i == 0:
                    name = attribute.text
                elif i == 1:
                    phones = attribute.text
                elif i == 2:
                    emails = attribute.text
                elif i == 3:
                    address = attribute.text
                i += 1
            customers.append(Customer(name, username, address, emails, phones))
        return customers

    def parse_accounts_html_to_objects(self, accounts_html: str) -> List[Account]:
        """Iterate over the accounts' html, and create and return Account objects."""
        accounts = list()
        soup = BeautifulSoup(accounts_html, 'html.parser')
        acts = soup.find_all('li', attrs={'class':'collection-item avatar'})
        for act in acts:
            name = act.find('span', attrs={'class':'title'}).text
            number_and_balance = act.find('p')
            number = number_and_balance.next_element.strip()
            balance = number_and_balance.find('span').text
            account_id = act.find('a')['href']
            account_id = account_id[account_id.index('/')+1:]
            accounts.append(Account(name, number, balance, account_id))
        return accounts

    def parse_statements_html_to_objects(self, statements_html: str) -> List[Statement]:
        """Iterate over the statements' html, and create and return Statement objects."""
        statements = list()
        soup = BeautifulSoup(statements_html, 'html.parser')
        thead = soup.find('thead')
        headers = thead.find_all('th')
        i = 0
        headerPositions = {}
        for header in headers:
            headerPositions[i] = header.text.lower()
            i += 1
        tbody = soup.find('tbody')
        stmts = tbody.find_all('tr')
        for stmt in stmts:
            attributes = stmt.find_all('td')
            date = ''
            amount = ''
            balance = ''
            concept = ''
            i = 0
            for attribute in attributes:
                # if the attribute is in the header,
                # user the header for reference
                if i in headerPositions:
                    if headerPositions[i] == 'statement':
                        concept = attribute.text
                    elif headerPositions[i] == 'date':
                        date = attribute.text
                    elif headerPositions[i] == 'amount':
                        amount = attribute.text
                    elif headerPositions[i] == 'balance':
                        balance = attribute.text
                # otherwise fall back to a set position
                else:
                    if i == 0:
                        concept = attribute.text
                    elif i == 1:
                        date = attribute.text
                    elif i == 2:
                        amount = attribute.text
                    elif i == 3:
                        balance = attribute.text
                i += 1
            statements.append(Statement(date, amount, balance, concept))
        return statements
