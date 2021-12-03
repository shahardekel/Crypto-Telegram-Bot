# Crypto-Telegram-Bot
A telegram bot, built with python, using APIs with various options to check the Bitcoin and Ethereum values and addresses.

In this folder, there are 3 files:
1. bot.py
2. functions.py
3. main.py

Packages used:
1. telegram
2. telegram.ext
3. requests
4. cv2
5. cryptoaddress

To run the bot, please follow these instructions:
1. run the file main.py on your terminal
2. open this URL: https://t.me/is_it_crypto_bot 
3. press /start

This bot contains a menu with 6 options:
1. Current Bitcoin currency- returns the current Bitcoin mean value from the last 24 hours.
2. Current Ethereum currency- returns the current Ethereum mean value from the last 24 hours.
3. Check My Bitcoin Address- asking for a Bitcoin address and return its balance in Satoshi and USD. If the address is not valid- returns an error massage.  
4. Check My Ethereum Address- asking for a Ethereum address and returns its balance in ETH and USD. If the address is not valid- returns an error massage.  
5. I don't know what coin I'm using!- In case you do not know if it is a Bitcoin or Ethereum address. Requests to enter some address and returns the corresponding value in Bitcoin or Ethereum, otherwise returns an error message.
6. Scan QR Code- Requests a photo of a QR code, if the code is a valid address (Bitcoin or Ethereum), returns its value, otherwise returns an error message

![image](https://user-images.githubusercontent.com/69580046/144607962-72e40527-5e5f-4f64-b05f-e80e81e41647.png)
