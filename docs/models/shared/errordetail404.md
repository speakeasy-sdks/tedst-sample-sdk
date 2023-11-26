# ErrorDetail404

error details description


## Fields

| Field                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `code`                                                                                                                                                                                                                                   | [Optional[shared.ErrorCodes404]](../../models/shared/errorcodes404.md)                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                       | The detailed error code associated with HTTP status 404.<br/>* `fx_quote_not_found`: The provided quote cannot be found in the service.<br/>* `fx_fee_configuration_not_found`: The configuration cannot be found for at least one of the fees.<br/> |
| `description`                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                       | Description of the error.                                                                                                                                                                                                                |