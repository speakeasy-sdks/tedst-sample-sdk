# Rates
(*rates*)

## Overview

The Rates API

### Available Operations

* [exchange_rate_v2](#exchange_rate_v2) - Exchange Rate V2
* [aggregated_exchange_rates](#aggregated_exchange_rates) - Fetch historic aggregated exchange rates

## exchange_rate_v2

This API fetches the interbank FX rate for a currency pair. Note that the rate provided does not include the Nium markup.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform()

req = operations.ExchangeRateV2Request(
    destination_currency_code='string',
    source_currency_code='string',
    x_request_id='{{$guid}}',
)

res = s.rates.exchange_rate_v2(req, "<YOUR_API_KEY_HERE>")

if res.exchange_rate_v2_response_dto is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ExchangeRateV2Request](../../models/operations/exchangeratev2request.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.ExchangeRateV2Security](../../models/operations/exchangeratev2security.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.ExchangeRateV2Response](../../models/operations/exchangeratev2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## aggregated_exchange_rates

This API will retrieve aggregated time series of historical exchange rate.

### Example Usage

```python
import dateutil.parser
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform()

req = operations.AggregatedExchangeRatesRequest(
    destination_currency_code='SGD',
    source_currency_code='USD',
    x_request_id='{{$guid}}',
)

res = s.rates.aggregated_exchange_rates(req, "<YOUR_API_KEY_HERE>")

if res.exchange_rates_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.AggregatedExchangeRatesRequest](../../models/operations/aggregatedexchangeratesrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.AggregatedExchangeRatesSecurity](../../models/operations/aggregatedexchangeratessecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.AggregatedExchangeRatesResponse](../../models/operations/aggregatedexchangeratesresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse400 | 400                     | application/json        |
| errors.ErrorResponse401 | 401                     | application/json        |
| errors.ErrorResponse403 | 403                     | application/json        |
| errors.ErrorResponse500 | 500                     | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |
