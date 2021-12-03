import requests
from cryptoaddress import get_crypto_address
import cv2

current_price_api='https://api.blockchain.com/v3/exchange/tickers' # for current prices of BTC and ETH
balance_bitcoin= "https://blockchain.info/q/addressbalance" # for BTC balance for a specific address
balance_etereum="https://api.etherscan.io/api?module=account&action=balance&address=" # for ETH balance for a specific address


def get_crypto_balance(coin):
    """
    :param coin: the coin name- Bitcoin or Ethereum- string
    :return: current price in USD
    """
    response=requests.get(current_price_api).json() # json turn response to dictionary
    if coin=='Bitcoin':
        answer=list(filter(lambda coin: coin["symbol"] == 'BTC-USD', response))[0]['price_24h']

    if coin=='Ethereum':
        answer = list(filter(lambda coin: coin["symbol"] == 'ETH-USD', response))[0]['price_24h']

    ret="The {}'s value today is {}$".format(coin, answer)+"\n click /menu to go back"
    return ret


def balance_btc(address):
    """
    :param address: Bitcoin adress (string)
    :return: balance in satoshi and USD if valid, else returns a message
    """
    # 1 satoshi = 0.0005683 USD

    if check_if_valid_btc(address)[1]==1:
        url = requests.get(balance_bitcoin + '/' + address).json()
        sat_usd = 'The balance for this address is {} satoshi, which equals to {:.2f} USD.'.format(url, float(url) * 0.0005683)
        ans = check_if_valid_btc(address)[0] + "\n" + sat_usd + '\n' + "press /cancel and then /menu to check another stuff"

    elif check_if_valid_btc(address)[1]==0:
        ans=check_if_valid_btc(address)[0]

    return ans

def balance_eth(address):
    """
    :param address: Etereum adress (string)
    :return: balance in ETH and USD if valid, else returns a message
    """
    # 1 wei = 10^-18 ETH
    # 1 ETH = 4486.66 USD

    url=balance_etereum+address+"&tag=latest" \
                                "&apikey=R24IYE5DGV7JSAWQBYZ4R979DAD1KKXTTR" # my API key
    if check_if_valid_eth(address)[1]==1:
        d = requests.get(url).json()
        eth_wei_usd=(float(d['result'])/pow(10,18))
        eth_usd = 'The balance for this address is {:.2f} ETH, which equals to {:.2f} USD.'.format(eth_wei_usd, eth_wei_usd*4486.66)
        ans = check_if_valid_eth(address)[0] + "\n" + eth_usd + '\n' + "press /cancel and then /menu to check another stuff"

    elif check_if_valid_eth(address)[1]==0:
        ans=check_if_valid_eth(address)[0]

    return ans


def check_if_valid_btc(address):
    """
    for the "Check My Bitcoin Adress" button
    :param address: Bitcoin adress (string)
    :return: if this address is valid
    """
    try:
        bitcoin_address = get_crypto_address('BTC', address, network_type='mainnet')
        return ['🤖 Your address {} is a valid Bitcoin address!'.format(str(bitcoin_address)),1]

    except ValueError:
        return ["🤖 The is not a Bitcoin address! Let's start over! please click on /cancel and then /menu",0]


def check_if_valid_eth(address):
    """
    for the "Check My Ethereum Adress" button
        :param address: Etereum adress (string)
        :return: if this address is valid
    """
    try:
        eth_address = get_crypto_address('ETH', address)
        return ['🤖 Your address {} is a valid Ethereum address!'.format(str(eth_address)),1]

    except ValueError:
        return ["🤖 The address is invalid! Let's start over! please click on /cancel and then /menu",0]

def check_valid_general(address):
    """
    fot the "I don't know what coin I'm using! check my address and tell me!"
    :param address: Bitcoin, Ethereum or an invalid address
    :return: balance if valid --> goes to the balance_### functions
    """
    eth = check_if_valid_eth(address)[1]
    btc = check_if_valid_btc(address)[1]
    if eth==1:
        return balance_eth(address)
    elif btc==1:
        return balance_btc(address)
    else:
        return "🤖 your adress is not Bitcoin or Etereum addresses!\nplease check your address, or press /cancel and then /menu."

def check_QR(img):
    """
    :param img: a QR code photo (.jpg)
    :return: address balance if the QR is an address, else return error massage
    """
    image = cv2.imread(img)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image) # 'data'- the address

    if vertices_array is not None:
        return check_valid_general(data)

    else:
        return "There was some error"

