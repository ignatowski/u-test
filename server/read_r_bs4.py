import getopt, sys
from u_test.api_r import ApiR
from u_test.html_parser_bs4 import HtmlParserBs4
from u_test.printer import Printer



def main() -> None:
    "Gets and prints data."

    # get the username and password from the command line arguments
    username = ''
    password = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["username=","password="])
    except getopt.GetoptError as err:
        print('usage: read.py --username <username> --password <password>')
        print('error: ' + str(err))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--username':
            username = arg
        elif opt == '--password':
            password = arg

    # login
    api_r = ApiR(username, password)
    api_r.login()

    # get the customers html
    customers_html = api_r.get_customers_html()
    # parse the customers html into customer objects
    html_parser_bs4 = HtmlParserBs4()
    customers = html_parser_bs4.parse_customers_html_to_objects(customers_html, username)

    # get the accounts html
    accounts_html = api_r.get_accounts_html()
    accounts = html_parser_bs4.parse_accounts_html_to_objects(accounts_html)

    # get statements for each account
    for account in accounts:
        # get the statements html
        statements_html = api_r.get_statements_html(account.account_id)
        account.statements = html_parser_bs4.parse_statements_html_to_objects(statements_html)

    # print accounts, customers, and statements
    Printer(accounts, customers)



if __name__ == '__main__':
    main()
