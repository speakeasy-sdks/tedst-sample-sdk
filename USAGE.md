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