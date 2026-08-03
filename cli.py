print("CLI started")
import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type
)
from bot.logging_config import setup_logger


setup_logger()


parser = argparse.ArgumentParser(
    description="Binance Futures Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True,
    help="Trading pair (e.g., BTCUSDT)"
)

parser.add_argument(
    "--side",
    required=True,
    help="BUY or SELL"
)

parser.add_argument(
    "--type",
    required=True,
    help="MARKET or LIMIT"
)

parser.add_argument(
    "--quantity",
    type=float,
    required=True,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    type=float,
    help="Price for LIMIT orders"
)


args = parser.parse_args()


try:

    side = validate_side(args.side)

    order_type = validate_order_type(
        args.type
    )

    if (
        order_type == "LIMIT"
        and args.price is None
    ):
        raise ValueError(
            "Price is required for LIMIT orders."
        )

    client = get_client()

    response = place_order(
        client,
        args.symbol,
        side,
        order_type,
        args.quantity,
        args.price
    )

    print("\n===== ORDER SUMMARY =====")

    print(
        f"Symbol: {args.symbol}"
    )

    print(
        f"Side: {side}"
    )

    print(
        f"Type: {order_type}"
    )

    print(
        f"Quantity: {args.quantity}"
    )

    print(
        f"Order ID: {response['orderId']}"
    )

    print(
        f"Status: {response['status']}"
    )

    print(
        f"Executed Qty: {response['executedQty']}"
    )

    print(
        "\n✅ Order placed successfully!"
    )

except Exception as e:

    print(
        f"\n❌ Error: {e}"
    )