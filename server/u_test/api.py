from http import client, cookies
from urllib import request, parse



class Api:
    """A class used to make http requests."""

    base_url = 'test.unnax.com'
    base_login = '/login'
    customer_url = 'http://test.unnax.com/customer'
    account_url = 'http://test.unnax.com/account'
    statement_url = 'http://test.unnax.com/statements/'

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.sessionCookies = None

    def login(self) -> None:
        """Login the user and store their cookies."""
        conn = client.HTTPConnection(self.base_url)
        body = parse.urlencode({'username': self.username, 'password': self.password})
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
            }
        conn.request("POST", self.base_login, body, headers)
        res = conn.getresponse()
        if (res.status != 302):
            raise Exception('Unable to get login')
        rawCookies = res.getheader('Set-Cookie')
        self.sessionCookies = cookies.SimpleCookie()
        self.sessionCookies.load(rawCookies)
        conn.close()

    def get_customers_html(self) -> str:
        """Get and return the html from the customer page."""
        req =  request.Request(url=self.customer_url)
        req.add_header('Cookie', 'session=' + self.sessionCookies['session'].value)
        res = request.urlopen(req)
        if (res.getcode() != 200):
            raise Exception('Unable to get customers')
        return res.read().decode('utf-8')

    def get_accounts_html(self) -> str:
        """Get and return the html from the account page."""
        req =  request.Request(url=self.account_url)
        req.add_header('Cookie', 'session=' + self.sessionCookies['session'].value)
        res = request.urlopen(req)
        if (res.getcode() != 200):
            raise Exception('Unable to get accounts')
        return res.read().decode('utf-8')

    def get_statements_html(self, account_id: str) -> str:
        """Get and return the html from the statements page."""
        req =  request.Request(url=self.statement_url+account_id)
        req.add_header('Cookie', 'session=' + self.sessionCookies['session'].value)
        res = request.urlopen(req)
        if (res.getcode() != 200):
            raise Exception('Unable to get statements')
        return res.read().decode('utf-8')
