from binance.lib.utils import check_required_parameters


def convert_trade_history(self, startTime: int, endTime: int, **kwargs):
    """Convert Trade History (USER_DATA)

    Get convert history for a specific account.

    GET /sapi/v1/convert/tradeFlow

    https://binance-docs.github.io/apidocs/spot/en/#convert-endpoints

    Args:
        startTime (int)
        endTime (int)
    Keyword Args:
        limit (int, optional): Default Value: 100; Max Value: 1000
        recvWindow (int, optional)
    """
    check_required_parameters([[startTime, "startTime"], [endTime, "endTime"]])

    url_path = "/sapi/v1/convert/tradeFlow"
    payload = {"startTime": startTime, "endTime": endTime, **kwargs}
    return self.sign_request("GET", url_path, payload)


def convert_get_quote(self, fromAsset: str, toAsset: str, **kwargs):
    """Send quote request (USER_DATA)

    Request a quote for the requested token pairs.

    POST /sapi/v1/convert/getQuote

    https://binance-docs.github.io/apidocs/spot/en/#convert-endpoints

    Args:
        fromAsset (string)
        toAsset (string)
    Keyword Args:
        fromAmount (number, optional)
        toAmount (number, optional)
        validTime (number, optional)
        recvWindow (int, optional)
    """
    check_required_parameters([[fromAsset, "fromAsset"], [toAsset, "toAsset"]])

    url_path = "/sapi/v1/convert/getQuote"
    payload = {"fromAsset": fromAsset, "toAsset": toAsset, **kwargs}
    return self.sign_request("POST", url_path, payload)


def convert_accept_quote(self, quoteId: str, **kwargs):
    """Accept Quote (TRADE)

    Accept the offered quote by quote ID.

    POST /sapi/v1/convert/acceptQuote

    https://binance-docs.github.io/apidocs/spot/en/#convert-endpoints

    Args:
        quoteId (string)
    Keyword Args:
        recvWindow (int, optional)
    """
    check_required_parameters([[quoteId, "quoteId"]])

    url_path = "/sapi/v1/convert/acceptQuote"
    payload = {"quoteId": quoteId, **kwargs}
    return self.sign_request("POST", url_path, payload)