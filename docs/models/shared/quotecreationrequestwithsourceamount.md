# QuoteCreationRequestWithSourceAmount


## Fields

| Field                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conversion_schedule`                                                                                                                                                                                                                                 | [Optional[ConversionSchedule]](../../models/shared/conversionschedule.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                    | The time period after which the conversion should be settled.                                                                                                                                                                                         | immediate                                                                                                                                                                                                                                             |
| `destination_currency_code`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                    | 3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the destination amount.                                                                                                                                       | SGD                                                                                                                                                                                                                                                   |
| `lock_period`                                                                                                                                                                                                                                         | [Optional[LockPeriod]](../../models/shared/lockperiod.md)                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                    | The duration for which the quote remains valid after creation.                                                                                                                                                                                        | 15_mins                                                                                                                                                                                                                                               |
| `quote_type`                                                                                                                                                                                                                                          | [QuoteType](../../models/shared/quotetype.md)                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                    | The type of the quote.<br/>  * `balance_transfer`: Quote for transferring the balance from one currency to another within the same customer wallet.<br/>  * `payout`: Quote for transferring money to a registered beneficiary's wallet in another currency.<br/> |                                                                                                                                                                                                                                                       |
| `source_amount`                                                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                    | The source amount to be converted to the destination currency. This value is for reference only and will not be used as the actual conversion amount.                                                                                                 | 13.42                                                                                                                                                                                                                                                 |
| `source_currency_code`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                    | 3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the source amount.                                                                                                                                            | USD                                                                                                                                                                                                                                                   |