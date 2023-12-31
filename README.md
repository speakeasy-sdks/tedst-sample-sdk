# NIUM-Platform

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/tedst-sample-sdk.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/tedst-sample-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/tedst-sample-sdk.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform()

req = operations.CancelConversionRequest(
    request_body=operations.CancelConversionConversionCancelRequest(
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
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [conversions](docs/sdks/conversions/README.md)

* [cancel_conversion](docs/sdks/conversions/README.md#cancel_conversion) - Cancel Conversion
* [create_conversion](docs/sdks/conversions/README.md#create_conversion) - Create Conversion
* [fetch_conversion](docs/sdks/conversions/README.md#fetch_conversion) - Fetch Conversion by id

### [conversions_previous_version](docs/sdks/conversionspreviousversion/README.md)

* [balance_transferwithin_wallet](docs/sdks/conversionspreviousversion/README.md#balance_transferwithin_wallet) - Balance Transfer within Wallet

### [quotes](docs/sdks/quotes/README.md)

* [create_quote](docs/sdks/quotes/README.md#create_quote) - Create Quote
* [fetch_quote](docs/sdks/quotes/README.md#fetch_quote) - Fetch Quote by ID

### [quotes_previous_version](docs/sdks/quotespreviousversion/README.md)

* [exchange_rate_lockand_hold](docs/sdks/quotespreviousversion/README.md#exchange_rate_lockand_hold) - Exchange Rate Lock and Hold
* [exchange_rate_with_markup](docs/sdks/quotespreviousversion/README.md#exchange_rate_with_markup) - Exchange Rate With Markup

### [rates](docs/sdks/rates/README.md)

* [exchange_rate_v2](docs/sdks/rates/README.md#exchange_rate_v2) - Exchange Rate V2
* [aggregated_exchange_rates](docs/sdks/rates/README.md#aggregated_exchange_rates) - Fetch historic aggregated exchange rates
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


## Example

```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform()

req = operations.CancelConversionRequest(
    request_body=operations.CancelConversionConversionCancelRequest(
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

except (cancelConversion_400ApplicationJSON_object) as e:
    print(e) # handle exception
except (cancelConversion_401ApplicationJSON_object) as e:
    print(e) # handle exception
except (cancelConversion_403ApplicationJSON_object) as e:
    print(e) # handle exception
except (cancelConversion_404ApplicationJSON_object) as e:
    print(e) # handle exception

except (cancelConversion_500ApplicationJSON_object) as e:
    print(e) # handle exception

if res.conversion_cancel_response is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://gatewaysandbox.nium.com/n1` | None |

For example:


```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform(
    server_idx=0
)

req = operations.CancelConversionRequest(
    request_body=operations.CancelConversionConversionCancelRequest(
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


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import nium_platform
from nium_platform.models import operations

s = nium_platform.NIUMPlatform(
    server_url="https://gatewaysandbox.nium.com/n1"
)

req = operations.CancelConversionRequest(
    request_body=operations.CancelConversionConversionCancelRequest(
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
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import nium_platform
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = nium_platform.NIUMPlatform(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
