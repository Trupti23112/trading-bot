from binance.enums import *


def place_order(
    client,
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = TIME_IN_FORCE_GTC

    return client.futures_create_order(**params)