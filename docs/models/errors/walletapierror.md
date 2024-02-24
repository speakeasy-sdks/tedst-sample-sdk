# WalletAPIError


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     | Example                                                         |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `errors`                                                        | List[*str*]                                                     | :heavy_minus_sign:                                              | List of errors occurred.                                        | [<br/>"field1 is not valid",<br/>"field2 is not valid"<br/>]    |
| `message`                                                       | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Error message descriptor.                                       | Error message descriptor.                                       |
| `status`                                                        | [Optional[errors.Status]](../../models/errors/status.md)        | :heavy_minus_sign:                                              | HttpStatus of the request : BAD_REQUEST, INTERNAL_SERVER_ERROR. | BAD_REQUEST                                                     |