# Crypto-Telegram-Bot
<h2>A telegram bot, built with python, using APIs with various options to check the Bitcoin and Ethereum values and addresses</h2>

[![Python 3.8](https://img.shields.io/badge/python-3.8-red.svg)](https://www.python.org/downloads/release/python-380/)
[![Try it on telegram](https://img.shields.io/badge/try%20it-on%20telegram-0088cc.svg)](http://t.me/badgemakerbot)

In this folder, there are 3 files:
1. bot.py - build bot configurations and functionalities
2. functions.py - utilities for bot functions
3. main.py - run the bot

<h3>Packages used:</h3><br>
1. telegram<br>
2. telegram.ext<br>
3. requests<br>
4. cv2<br>
5. cryptoaddress<br>

<h3>To run the bot, please follow these instructions:</h3>
1. run the file main.py on your terminal<br>
2. open this URL: https://t.me/is_it_crypto_bot <br>
3. press /start
<br><br>
<h3>This bot contains a menu with 6 options:<br></h3>
1. <b>Current Bitcoin currency</b>- returns the current Bitcoin mean value from the last 24 hours.<br>
2. <b>Current Ethereum currency</b>- returns the current Ethereum mean value from the last 24 hours.<br>
3. <b>Check My Bitcoin Address</b>- asking for a Bitcoin address and return its balance in Satoshi and USD. If the address is not valid- returns an error massage.<br>  
4. <b>Check My Ethereum Address</b>- asking for a Ethereum address and returns its balance in ETH and USD. If the address is not valid- returns an error massage.<br>
5. <b>I don't know what coin I'm using!</b>- In case you do not know if it is a Bitcoin or Ethereum address. Requests to enter some address and returns the corresponding value in Bitcoin or Ethereum, otherwise returns an error message.<br>
6. <b>Scan QR Code</b>- Requests a photo of a QR code, if the code is a valid address (Bitcoin or Ethereum), returns its value, otherwise returns an error message
