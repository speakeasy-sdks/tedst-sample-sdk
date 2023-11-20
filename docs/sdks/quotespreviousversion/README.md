# QuotesPreviousVersion
(*quotes_previous_version*)

## Overview

The previous version of the Quotes API

### Available Operations

* [exchange_rate_lockand_hold](#exchange_rate_lockand_hold) - Exchange Rate Lock and Hold
* [exchange_rate_with_markup](#exchange_rate_with_markup) - Exchange Rate With Markup

## exchange_rate_lockand_hold

This API allows you to fetch exchange rate, and lock and hold the rates till a certain amount of time.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform()

req = operations.ExchangeRateLockandHoldRequest(
    client_hash_id='{{clientHashId}}',
    customer_hash_id='string',
    destination_currency='string',
    source_currency='string',
    wallet_hash_id='string',
    x_request_id='{{$guid}}',
)

res = s.quotes_previous_version.exchange_rate_lockand_hold(req, "")

if res.fx_hold_lock_response_content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ExchangeRateLockandHoldRequest](../../models/operations/exchangeratelockandholdrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ExchangeRateLockandHoldSecurity](../../models/operations/exchangeratelockandholdsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.ExchangeRateLockandHoldResponse](../../models/operations/exchangeratelockandholdresponse.md)**
### Errors

| Error Object          | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.WalletAPIError | 400,404,500           | application/json      |
| errors.SDKError       | 400-600               | */*                   |

## exchange_rate_with_markup

This API fetches the exchange rate between source currency and destination currency. If either source or destination amount is provided, the equivalent amount will also be returned. Note that you may not send both sourceAmount and destinationAmount as query parameters together. If both are provided, sourceAmount shall be taken for conversion.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform()

req = operations.ExchangeRateWithMarkupRequest(
    client_hash_id='string',
    destination_currency_code='string',
    source_currency_code='string',
    x_request_id='{{$guid}}',
)

res = s.quotes_previous_version.exchange_rate_with_markup(req, "")

if res.exchange_rate_v2_response_dto is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ExchangeRateWithMarkupRequest](../../models/operations/exchangeratewithmarkuprequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ExchangeRateWithMarkupSecurity](../../models/operations/exchangeratewithmarkupsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ExchangeRateWithMarkupResponse](../../models/operations/exchangeratewithmarkupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
