import sys
from html.parser import HTMLParser
from .models import Customer, Account, Statement
from typing import List



class HtmlParserCustomers(HTMLParser):
    """A class used to parse customers html to Customer objects."""

    def __init__(self, username: str = '') -> None:
        HTMLParser.__init__(self)
        # customers data
        self.customer_doc = username
        self.customers = list()
        self.customer_object_entered = False
        self.customer_attribute_entered = False
        self.customer_li_count = 0
        self.customer_name, self.customer_address, self.customer_emails, self.customer_phones = ('','','','')

    def handle_starttag(self, tag: str, attrs: List[tuple]) -> None:
        """Set instance properties based on opening html tags."""
        # beginning of customer html
        if tag == 'ul':
            for name, value in attrs:
                if name == 'class' and value == 'collection with-header':
                    self.customer_object_entered = True
        # beginning of customer attribute html
        if self.customer_object_entered == True and tag == 'li':
            self.customer_attribute_entered = True
            self.customer_li_count += 1

    def handle_endtag(self, tag: str) -> None:
        """Set instance properties based on closing html tags."""
        # end of customer html
        if tag == 'ul' and self.customer_object_entered == True:
            self.customers.append(Customer(self.customer_name, self.customer_doc, self.customer_address, self.customer_emails, self.customer_phones))
            self.customer_object_entered = False
            self.customer_attribute_entered = False
            self.customer_li_count = 0
            self.customer_name, self.customer_address, self.customer_emails, self.customer_phones = ('','','','')

    def handle_data(self, data: str) -> None:
        """Set instance properties based on html data."""
        # customer attribute text that's not empty
        if self.customer_attribute_entered == True and data.strip():
            if self.customer_li_count == 1:
                self.customer_name = data
            elif self.customer_li_count == 2:
                self.customer_phones = data
            elif self.customer_li_count == 3:
                self.customer_emails = data
            elif self.customer_li_count == 4:
                self.customer_address = data



class HtmlParserAccounts(HTMLParser):
    """A class used to parse accounts html to Account objects."""

    def __init__(self) -> None:
        HTMLParser.__init__(self)
        # accounts data
        self.accounts = list()
        self.account_object_entered = False
        self.account_attributes_entered = False
        self.account_attribute_count = 0
        self.account_name, self.account_number, self.account_balance, self.account_id = ('','','','')

    def handle_starttag(self, tag: str, attrs: List[tuple]) -> None:
        """Set instance properties based on opening html tags."""
        # beginning of account html
        if tag == 'ul':
            for name, value in attrs:
                if name == 'class' and value == 'collection':
                    self.account_object_entered = True
        # beginning of account attribute html
        if self.account_object_entered == True and tag == 'li':
            self.account_attributes_entered = True
        # account id
        if self.account_attributes_entered == True and tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.account_id = value[value.index('/')+1:]

    def handle_endtag(self, tag: str) -> None:
        """Set instance properties based on closing html tags."""
        # end of account html
        if tag == 'li' and self.account_attributes_entered == True:
            self.accounts.append(Account(self.account_name, self.account_number, self.account_balance, self.account_id))
            self.account_attributes_entered = False
            self.account_attribute_count = 0
            self.account_name, self.account_address, self.account_emails, self.account_phones = ('','','','')
        if tag == 'ul' and self.account_object_entered == True:
            self.account_object_entered = False

    def handle_data(self, data: str) -> None:
        """Set instance properties based on html data."""
        # account attribute text that's not empty
        if self.account_attributes_entered == True and data.strip():
            self.account_attribute_count += 1
            if self.account_attribute_count == 1:
                self.account_name = data
            elif self.account_attribute_count == 2:
                self.account_number = data
            elif self.account_attribute_count == 3:
                self.account_balance = data



class HtmlParserStatements(HTMLParser):
    """A class used to parse statements html to Statement objects."""

    def __init__(self) -> None:
        HTMLParser.__init__(self)
        # statements data
        self.statements = list()
        self.statement_headerPositions = {}
        self.statement_thead_entered = False
        self.statement_thead_td_entered = False
        self.statement_thead_count = 0
        self.statements_html_entered = False
        self.statement_object_entered = False
        self.statement_attributes_entered = False
        self.statement_attribute_count = 0
        self.statement_date, self.statement_amount, self.statement_balance, self.statement_concept = ('','','','')

    def handle_starttag(self, tag: str, attrs: List[tuple]) -> None:
        """Set instance properties based on opening html tags."""
        # beginning of statement html
        if tag == 'thead':
            self.statement_thead_entered = True
        if tag == 'td' and self.statement_thead_entered == True:
            self.statement_thead_td_entered = True
            self.statement_thead_count += 1
        if tag == 'tbody':
            self.statements_html_entered = True
        # beginning of statement object
        if tag == 'tr' and self.statements_html_entered == True:
            self.statement_object_entered = True
        # beginning of statement attribute html
        if self.statement_object_entered == True and tag == 'td':
            self.statement_attributes_entered = True
            self.statement_attribute_count += 1

    def handle_endtag(self, tag: str) -> None:
        """Set instance properties based on closing html tags."""
        # end of statement header html
        if tag == 'thead' and self.statement_thead_entered == True:
            self.statement_thead_entered = False
            self.statement_thead_td_entered = False
            self.statement_thead_count = 0
        # end of statement object html
        if tag == 'tr' and self.statement_attributes_entered == True:
            self.statements.append(Statement(self.statement_date, self.statement_amount, self.statement_balance, self.statement_concept))
            self.statement_object_entered = False
            self.statement_attributes_entered = False
            self.statement_attribute_count = 0
            self.statement_date, self.statement_amount, self.statement_balance, self.statement_concept = ('','','','')
        # end of statements html
        if tag == 'tbody':
            self.statements_html_entered = False

    def handle_data(self, data: str) -> None:
        """Set instance properties based on html data."""
        # statement header text that's not empty
        if self.statement_thead_td_entered == True and data.strip():
                self.statement_headerPositions[self.statement_thead_count] = data.lower()
        # statement attribute text that's not empty
        if self.statement_attributes_entered == True and data.strip():
            # if the attribute is in the header,
            # user the header for reference
            if self.statement_attribute_count in self.statement_headerPositions:
                if self.statement_headerPositions[self.statement_attribute_count] == 'statement':
                    self.statement_concept = data
                elif self.statement_headerPositions[self.statement_attribute_count] == 'date':
                    self.statement_date = data
                elif self.statement_headerPositions[self.statement_attribute_count] == 'amount':
                    self.statement_amount = data
                elif self.statement_headerPositions[self.statement_attribute_count] == 'balance':
                    self.statement_balance = data
            # otherwise fall back to a set position
            else:
                if self.statement_attribute_count == 1:
                    self.statement_concept = data
                elif self.statement_attribute_count == 2:
                    self.statement_date = data
                elif self.statement_attribute_count == 3:
                    self.statement_amount = data
                elif self.statement_attribute_count == 4:
                    self.statement_balance = data



class HtmlObjects:
    """A class used to parse html to objects."""

    def __init__(self) -> None:
        pass

    def parse_customers_html_to_objects(self, customers_html: str, username: str) -> List[Customer]:
        """Iterate over the customers' html, and create and return Customer objects."""
        html_parser_customers = HtmlParserCustomers(username)
        html_parser_customers.feed(customers_html)
        html_parser_customers.close()
        return html_parser_customers.customers

    def parse_accounts_html_to_objects(self, accounts_html: str) -> List[Account]:
        """Iterate over the accounts' html, and create and return Account objects."""
        html_parser_accounts = HtmlParserAccounts()
        html_parser_accounts.feed(accounts_html)
        html_parser_accounts.close()
        return html_parser_accounts.accounts

    def parse_statements_html_to_objects(self, statements_html: str) -> List[Statement]:
        """Iterate over the statements' html, and create and return Statement objects."""
        html_parser_statements = HtmlParserStatements()
        html_parser_statements.feed(statements_html)
        html_parser_statements.close()
        return html_parser_statements.statements
