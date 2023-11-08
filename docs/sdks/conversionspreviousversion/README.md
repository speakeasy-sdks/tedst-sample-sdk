# ConversionsPreviousVersion
(*.conversions_previous_version*)

## Overview

The Previous version of the Conversions API

### Available Operations

* [balance_transferwithin_wallet](#balance_transferwithin_wallet) - Balance Transfer within Wallet

## balance_transferwithin_wallet

This API allows you to transfer the balance from one currency to another within the same customer wallet.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform()

req = operations.BalanceTransferwithinWalletRequest(
    wallet_transfer_dto=shared.WalletTransferDto(
        amount=10,
        customer_comments='Changed SGD to INR during Travel',
        destination_amount=20,
        destination_currency='INR',
        quote_id='UUID',
        source_currency='SGD',
    ),
    client_hash_id='string',
    customer_hash_id='string',
    wallet_hash_id='string',
    x_request_id='{{$guid}}',
)

res = s.conversions_previous_version.balance_transferwithin_wallet(req, "")

if res.wallet_transfer_response_dto is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.BalanceTransferwithinWalletRequest](../../models/operations/balancetransferwithinwalletrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.BalanceTransferwithinWalletSecurity](../../models/operations/balancetransferwithinwalletsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.BalanceTransferwithinWalletResponse](../../models/operations/balancetransferwithinwalletresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
