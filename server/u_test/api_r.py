import requests



class ApiR:
    """A class used to make http requests."""

    login_url = 'http://test.unnax.com/login'
    customer_url = 'http://test.unnax.com/customer'
    account_url = 'http://test.unnax.com/account'
    statement_url = 'http://test.unnax.com/statements/'

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.ses = requests.session()

    def login(self) -> None:
        """Login the user and create a session."""
        data = {'username': self.username, 'password': self.password}
        res = self.ses.post(self.login_url, data=data, allow_redirects=False)
        if (res.status_code != 302):
            raise Exception('Unable to login')

    def get_customers_html(self) -> str:
        """Get and return the html from the customer page."""
        res = self.ses.get(self.customer_url)
        if (res.status_code != 200):
            raise Exception('Unable to get customer')
        return res.text

    def get_accounts_html(self) -> str:
        """Get and return the html from the account page."""
        res = self.ses.get(self.account_url)
        if (res.status_code != 200):
            raise Exception('Unable to get accounts')
        return res.text

    def get_statements_html(self, account_id: str) -> str:
        """Get and return the html from the statements page."""
        res = self.ses.get(self.statement_url+account_id)
        if (res.status_code != 200):
            raise Exception('Unable to get statements')
        return res.text
