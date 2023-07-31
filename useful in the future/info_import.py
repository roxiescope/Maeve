from lxml import html
import requests
import mintapi

def example():
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.content)

    #This will create a list of buyers:
    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    #This will create a list of prices:
    prices = tree.xpath('//span[@class="item-price"]/text()')

    print('Buyers: ', buyers)
    print('Prices: ', prices)


mint = mintapi.Mint(
    'steinroxanna@gmail.com',
    'Tiger1996=',
    mfa_method='sms',
    headless=False,
    mfa_input_callback=None,
    session_path=None,
    imap_account=None,
    imap_password=None,
    imap_server=None,
    imap_folder='INBOX',
    wait_for_sync=False,
    wait_for_sync_timeout=300,
)

# Get basic account information
mint.get_accounts()

# Get extended account detail at the expense of speed - requires an
# additional API call for each account
mint.get_accounts(True)

# Get budget information
mint.get_budgets()

# Get transactions
mint.get_transactions()  # as pandas dataframe
mint.get_transactions_csv(include_investment=False)  # as raw csv data
mint.get_transactions_json(include_investment=False, skip_duplicates=False)

# Get transactions for a specific account
# accounts = mint.get_accounts(True)
# for account in accounts:
#     mint.get_transactions_csv(id=account["id"])
#     mint.get_transactions_json(id=account["id"])

# Get net worth
print(mint.get_net_worth())

# Get credit score
#mint.get_credit_score()

# Get bills
#mint.get_bills()

# Get investments (holdings and transactions)
#mint.get_invests_json()

# Close session and exit cleanly from selenium/chromedriver
#mint.close()

# Initiate an account refresh
#mint.initiate_account_refresh()