# NIUM-Platform

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/tedst-sample-sdk.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/tedst-sample-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install NIUM-Platform
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform()

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

res = s.conversions.cancel_conversion(req, "")

if res.conversion_cancel_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [conversions](docs/sdks/conversions/README.md)

* [cancel_conversion](docs/sdks/conversions/README.md#cancel_conversion) - Cancel Conversion
* [create_conversion](docs/sdks/conversions/README.md#create_conversion) - Create Conversion
* [fetch_conversion](docs/sdks/conversions/README.md#fetch_conversion) - Fetch Conversion by id

### [quotes_previous_version](docs/sdks/quotespreviousversion/README.md)

* [exchange_rate_lockand_hold](docs/sdks/quotespreviousversion/README.md#exchange_rate_lockand_hold) - Exchange Rate Lock and Hold
* [exchange_rate_with_markup](docs/sdks/quotespreviousversion/README.md#exchange_rate_with_markup) - Exchange Rate With Markup

### [conversions_previous_version](docs/sdks/conversionspreviousversion/README.md)

* [balance_transferwithin_wallet](docs/sdks/conversionspreviousversion/README.md#balance_transferwithin_wallet) - Balance Transfer within Wallet

### [quotes](docs/sdks/quotes/README.md)

* [create_quote](docs/sdks/quotes/README.md#create_quote) - Create Quote
* [fetch_quote](docs/sdks/quotes/README.md#fetch_quote) - Fetch Quote by ID

### [rates](docs/sdks/rates/README.md)

* [exchange_rate_v2](docs/sdks/rates/README.md#exchange_rate_v2) - Exchange Rate V2
* [aggregated_exchange_rates](docs/sdks/rates/README.md#aggregated_exchange_rates) - Fetch historic aggregated exchange rates
<!-- End Available Resources and Operations [operations] -->



<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorResponse400 | 400                     | application/json        |
| errors.ErrorResponse401 | 401                     | application/json        |
| errors.ErrorResponse403 | 403                     | application/json        |
| errors.ErrorResponse404 | 404                     | application/json        |
| errors.ErrorResponse500 | 500                     | application/json        |
| errors.SDKError         | 400-600                 | */*                     |

### Example

```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform()

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

res = None
try:
    res = s.conversions.cancel_conversion(req, "")
except (errors.ErrorResponse400) as e:
    print(e) # handle exception
except (errors.ErrorResponse401) as e:
    print(e) # handle exception
except (errors.ErrorResponse403) as e:
    print(e) # handle exception
except (errors.ErrorResponse404) as e:
    print(e) # handle exception

except (errors.ErrorResponse500) as e:
    print(e) # handle exception
except (errors.SDKError) as e:
    print(e) # handle exception


if res.conversion_cancel_response is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://gatewaysandbox.nium.com/` | None |

#### Example

```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform(
    server_idx=0,
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

res = s.conversions.cancel_conversion(req, "")

if res.conversion_cancel_response is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform(
    server_url="https://gatewaysandbox.nium.com/",
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

res = s.conversions.cancel_conversion(req, "")

if res.conversion_cancel_response is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import nium_platform
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = nium_platform.NIUMPlatform(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `default` | apiKey    | API key   |

To authenticate with the API the `default` parameter must be set when initializing the SDK client instance. For example:
```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform()

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

res = s.conversions.cancel_conversion(req, "")

if res.conversion_cancel_response is not None:
    # handle response
    pass
```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import nium_platform
from nium_platform.models import operations, shared

s = nium_platform.NIUMPlatform()

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

res = s.conversions.cancel_conversion(req, "")

if res.conversion_cancel_response is not None:
    # handle response
    pass
```
<!-- End Authentication [security] --><!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
