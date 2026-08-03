# Binance Futures Trading Bot

A command-line trading bot built with Python and the Binance API. The bot allows users to place market and limit orders on Binance Futures Testnet using simple terminal commands.

---

## Features

- Place market and limit orders on Binance Futures Testnet
- Command-line interface (CLI)
- Input validation for symbols, quantities, and order types
- Error handling for invalid requests and API failures
- Logging for order tracking and debugging
- Modular and reusable code structure

---

## Project Structure

```text
trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── bot.log
│
├── cli.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Technologies Used

- Python
- Binance API
- python-binance
- python-dotenv
- argparse
- logging
- Git and GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Trupti23112/trading-bot.git
```

Move to the project folder:

```bash
cd trading-bot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root and add your Binance Testnet credentials:

```text
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Running the Bot

### Place a market order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a limit order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 115000
```

### View all available commands

```bash
python cli.py --help
```

---

## Sample Output

```text
===== ORDER SUMMARY =====

Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order ID: 27777646746
Status: NEW
Executed Qty: 0.0000

Order placed successfully!
```

---

## Validation and Error Handling

The bot validates:

- Trading symbol
- Order type
- Buy/sell side
- Quantity and price values

Errors from the Binance API are handled gracefully and displayed to the user.

---

## Logging

All important events and order details are stored in:

```text
logs/bot.log
```

Logs help in debugging and monitoring the bot's activity.

---



---
## Demo

A screen recording demonstrating the successful execution of the Binance Futures Trading Bot is included in this repository.

The demo showcases:

- Running the bot from the command line
- Placing market and limit orders on Binance Futures Testnet
- Input validation and error handling
- Order summary and status output
- Logging of transactions

Video file: `demo.mp4`

## Disclaimer

This project is intended for educational purposes only and uses the Binance Testnet environment. Do not use real funds without proper testing.
