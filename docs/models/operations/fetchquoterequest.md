# FetchQuoteRequest


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `client_hash_id`                     | *str*                                | :heavy_check_mark:                   | Unique identifier of the client.     | abc12345-5d6e-0a8b-c8d7-3a7706a0c312 |
| `quote_id`                           | *str*                                | :heavy_check_mark:                   | N/A                                  | quote_1234567890abcdefABCDEF         |
| `x_request_id`                       | *Optional[str]*                      | :heavy_minus_sign:                   | Enter a unique UUID value            | {{$guid}}                            |