# Conversions
(*conversions*)

## Overview

The Conversions API

### Available Operations

* [cancel_conversion](#cancel_conversion) - Cancel Conversion
* [create_conversion](#create_conversion) - Create Conversion
* [fetch_conversion](#fetch_conversion) - Fetch Conversion by id

## cancel_conversion

This API allows you to cancel a conversion prior to the execution time.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform(
    default="<YOUR_API_KEY_HERE>",
)

req = operations.CancelConversionRequest(
    conversion_cancel_request=shared.ConversionCancelRequest(
        cancellation_comment='Cancelling due to change of plans.',
    ),
    client_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    conversion_id='conversion_1234567890abcdefABCDEF',
    customer_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    wallet_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    x_request_id='{{$guid}}',
)

res = s.conversions.cancel_conversion(req)

if res.conversion_cancel_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CancelConversionRequest](../../models/operations/cancelconversionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CancelConversionResponse](../../models/operations/cancelconversionresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse400 | 400                     | application/json        |
| errors.ErrorResponse401 | 401                     | application/json        |
| errors.ErrorResponse403 | 403                     | application/json        |
| errors.ErrorResponse404 | 404                     | application/json        |
| errors.ErrorResponse500 | 500                     | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## create_conversion

This API allows you to convert the balance from one currency to another within the same customer wallet either at the current market rate or using a previous exchange rate quote. This API allows you to select a settlement schedule for the conversion.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform(
    default="<YOUR_API_KEY_HERE>",
)

req = operations.CreateConversionRequest(
    conversion_creation_request=shared.ConversionCreationRequestSchemasWithSourceAmount(
        customer_comment='Converting SGD to INR during Travel.',
        quote_id='quote_1234567890abcdefABCDEF',
        source_amount=13.42,
    ),
    client_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    customer_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    wallet_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    x_request_id='{{$guid}}',
)

res = s.conversions.create_conversion(req)

if res.conversion_creation_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateConversionRequest](../../models/operations/createconversionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateConversionResponse](../../models/operations/createconversionresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse400 | 400                     | application/json        |
| errors.ErrorResponse401 | 401                     | application/json        |
| errors.ErrorResponse403 | 403                     | application/json        |
| errors.ErrorResponse404 | 404                     | application/json        |
| errors.ErrorResponse500 | 500                     | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## fetch_conversion

This API will retrieve an existing conversion with the conversionId.

### Example Usage

```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform(
    default="<YOUR_API_KEY_HERE>",
)

req = operations.FetchConversionRequest(
    client_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    conversion_id='conversion_1234567890abcdefABCDEF',
    customer_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    wallet_hash_id='abc12345-5d6e-0a8b-c8d7-3a7706a0c312',
    x_request_id='{{$guid}}',
)

res = s.conversions.fetch_conversion(req)

if res.conversion_creation_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.FetchConversionRequest](../../models/operations/fetchconversionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.FetchConversionResponse](../../models/operations/fetchconversionresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse400 | 400                     | application/json        |
| errors.ErrorResponse401 | 401                     | application/json        |
| errors.ErrorResponse403 | 403                     | application/json        |
| errors.ErrorResponse404 | 404                     | application/json        |
| errors.ErrorResponse500 | 500                     | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |
