from ..models import Customer, Account, Statement
from datetime import datetime
import unittest



class TestCustomer(unittest.TestCase):
    """Test the Customer class."""

    def __init__(self, *args, **kwargs) -> None:
        """Test that a Customer object can be created."""
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.name = 'Test Name'
        self.participation = 'Titular'
        self.doc = 'Test Doc'
        self.address = 'Test Address'
        self.emails = 'Test Emails'
        self.phones = 'Test Phones'
        self.customer = Customer(self.name, self.doc, self.address, self.emails, self.phones)

    def test_customer_name(self) -> None:
        """Test that the customer name was set correctly."""
        self.assertEqual(self.customer.name, self.name)

    def test_customer_participation(self) -> None:
        """Test that the customer participation was set correctly."""
        self.assertEqual(self.customer.participation, self.participation)

    def test_customer_doc(self) -> None:
        """Test that the customer doc was set correctly."""
        self.assertEqual(self.customer.doc, self.doc)

    def test_customer_address(self) -> None:
        """Test that the customer address was set correctly."""
        self.assertEqual(self.customer.address, self.address)

    def test_customer_emails(self) -> None:
        """Test that the customer emails was set correctly."""
        self.assertEqual(self.customer.emails, self.emails)

    def test_customer_phones(self) -> None:
        """Test that the customer phones was set correctly."""
        self.assertEqual(self.customer.phones, self.phones)



class TestAccount(unittest.TestCase):
    """Test the Account class."""

    def __init__(self, *args, **kwargs) -> None:
        """Test that an Account object can be created."""
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.name = 'Test Name'
        self.number = '1234'
        self.currency = 'EUR'
        self.balance = '€100'
        self.account_id = '1'
        self.statements = list()
        self.account = Account(self.name, self.number, self.balance, self.account_id)

    def test_account_name(self) -> None:
        """Test that the account name was set correctly."""
        self.assertEqual(self.account.name, self.name)

    def test_account_number(self) -> None:
        """Test that the account number was set correctly."""
        self.assertEqual(self.account.number, self.number)

    def test_account_currency(self) -> None:
        """Test that the account currency was set correctly."""
        self.assertEqual(self.account.currency, self.currency)

    def test_account_balance(self) -> None:
        """Test that the account balance was set correctly."""
        self.assertEqual(self.account.balance, self.balance)

    def test_account_statements(self) -> None:
        """Test that the account statements was set correctly."""
        self.assertEqual(self.account.statements, self.statements)



class TestStatement(unittest.TestCase):
    """Test the Statement class."""

    def __init__(self, *args, **kwargs) -> None:
        """Test that an Statement object can be created."""
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.date = '31/12/2010'
        self.amount = '€10'
        self.balance = '€100.2'
        self.concept = 'Test Concept'
        self.statement = Statement(self.date, self.amount, self.balance, self.concept)

    def test_statement_date(self) -> None:
        """Test that the statement date was set correctly."""
        self.assertEqual(self.statement.date, datetime.strptime(self.date, '%d/%m/%Y'))

    def test_statement_amount(self) -> None:
        """Test that the statement amount was set correctly."""
        self.assertEqual(self.statement.amount, self.amount)

    def test_statement_balance(self) -> None:
        """Test that the statement balance was set correctly."""
        self.assertEqual(self.statement.balance, self.balance)

    def test_statement_concept(self) -> None:
        """Test that the statement concept was set correctly."""
        self.assertEqual(self.statement.concept, self.concept)



if __name__ == '__main__':
    unittest.main()
