import datetime, os, re



class Customer:
    """A Customer object."""

    def __init__(self, name: str, doc: str, address: str, emails: str, phones: str) -> None:
        self.name = name
        self.participation = 'Titular'
        self.doc = doc
        self.address = address
        self.emails = emails
        self.phones = phones

    def __str__(self) -> str:
        return (
            '\t\t\tName: ' + self.name + os.linesep +
            '\t\t\tParticipation: ' + self.participation + os.linesep +
            '\t\t\tDoc: ' + self.doc + os.linesep +
            '\t\t\tAddress: ' + self.address + os.linesep +
            '\t\t\tEmails: ' + self.emails + os.linesep +
            '\t\t\tPhones: ' + self.phones + os.linesep
        )



class Account:
    """An Account object."""

    def __init__(self, name: str, number: str, balance: str, account_id: str) -> None:
        self.name = name
        self.number = number
        self.currency = self.determine_currency(balance)
        self.balance = balance
        self.account_id = account_id
        self.statements = list()

    def __str__(self) -> str:
        return (
            '\t\tName: ' + self.name + os.linesep +
            '\t\tNumber: ' + self.number + os.linesep +
            '\t\tCurrency: ' + self.currency + os.linesep +
            '\t\tBalance: ' + re.sub("[^0-9.]", "", self.balance) + os.linesep
        )

    def determine_currency(self, balance: str) -> str:
        """Check the currency symbol of the balance and return the three letter text representation."""
        if (balance[0] == '€'):
            return 'EUR'
        return ''



class Statement:
    """A Statement object."""

    def __init__(self, date: str, amount: str, balance: str, concept: str) -> None:
        self.date = self.format_date(date)
        self.amount = amount
        self.balance = balance
        self.concept = concept

    def __str__(self) -> str:
        return (
            '\t\t' + 
            self.date.strftime('%Y-%m-%d').ljust(11) + '|' + 
            '{0:-.1f}'.format(self.amount).center(8) + '|' + 
            ' ' + '{0:-.0f}'.format(self.balance).ljust(8) + '|' + 
            ' ' + self.concept + 
            os.linesep
        )

    def format_date(self, date: str) -> datetime:
        """Take a date string in format '%d/%m/%Y' and return a datetime object."""
        return datetime.datetime.strptime(date, '%d/%m/%Y')
