# Quotes
(*quotes*)

## Overview

The Quotes API

### Available Operations

* [create_quote](#create_quote) - Create Quote
* [fetch_quote](#fetch_quote) - Fetch Quote by ID

## create_quote

This API creates an FX quote for a currency pair according to the desired lock period and conversion schedule. The FX rate provided by this API includes the Nium markup and can be utilized for any FX conversion within the quote's validity period.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform()

req = operations.CreateQuoteRequest(
    quote_creation_request=shared.WithDestinationAmount(
    destination_currency_code='SGD',
    quote_type=shared.QuoteType.PAYOUT,
    source_currency_code='USD',
    conversion_schedule=shared.ConversionSchedule.IMMEDIATE,
    destination_amount=13.42,
    lock_period=shared.LockPeriod.FIFTEEN_MINS,
),
    client_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    x_request_id='{{$guid}}',
)

res = s.quotes.create_quote(req, "<YOUR_API_KEY_HERE>")

if res.quote_creation_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateQuoteRequest](../../models/operations/createquoterequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.CreateQuoteSecurity](../../models/operations/createquotesecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.CreateQuoteResponse](../../models/operations/createquoteresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse400 | 400                     | application/json        |
| errors.ErrorResponse401 | 401                     | application/json        |
| errors.ErrorResponse403 | 403                     | application/json        |
| errors.ErrorResponse404 | 404                     | application/json        |
| errors.ErrorResponse500 | 500                     | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## fetch_quote

This API allows to fetch a quote. A quote is used to identify the exchange rate, and associated markup and fees.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform()

req = operations.FetchQuoteRequest(
    client_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    quote_id='quote_1234567890abcdefABCDEF',
    x_request_id='{{$guid}}',
)

res = s.quotes.fetch_quote(req, "<YOUR_API_KEY_HERE>")

if res.quote_creation_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.FetchQuoteRequest](../../models/operations/fetchquoterequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.FetchQuoteSecurity](../../models/operations/fetchquotesecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.FetchQuoteResponse](../../models/operations/fetchquoteresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse400 | 400                     | application/json        |
| errors.ErrorResponse401 | 401                     | application/json        |
| errors.ErrorResponse403 | 403                     | application/json        |
| errors.ErrorResponse404 | 404                     | application/json        |
| errors.ErrorResponse500 | 500                     | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |
