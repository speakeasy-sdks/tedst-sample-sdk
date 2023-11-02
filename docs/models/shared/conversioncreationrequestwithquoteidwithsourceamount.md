# ConversionCreationRequestWithQuoteIDWithSourceAmount


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `customer_comment`                                                | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Free text comment for clients to record and track the conversion. | Converting SGD to INR during Travel.                              |
| `quote_id`                                                        | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Unique identifier of the quote.                                   | quote_1234567890abcdefABCDEF                                      |
| `source_amount`                                                   | *Optional[float]*                                                 | :heavy_minus_sign:                                                | The source amount to be converted to the destination currency.    | 13.42                                                             |