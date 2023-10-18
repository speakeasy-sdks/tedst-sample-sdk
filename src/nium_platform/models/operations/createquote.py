"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from nium_platform import utils
from typing import Optional


@dataclasses.dataclass
class CreateQuoteSecurity:
    default: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'x-api-key' }})
    


class CreateQuoteRequestBodyConversionSchedule(str, Enum):
    r"""The time period after which the conversion should be settled."""
    IMMEDIATE = 'immediate'
    END_OF_DAY = 'end_of_day'
    NEXT_DAY = 'next_day'
    TWO_DAYS = '2_days'

class CreateQuoteRequestBodyLockPeriod(str, Enum):
    r"""The duration for which the quote remains valid after creation."""
    FIVE_MINS = '5_mins'
    FIFTEEN_MINS = '15_mins'
    ONE_HOUR = '1_hour'
    FOUR_HOURS = '4_hours'
    EIGHT_HOURS = '8_hours'
    TWENTY_FOUR_HOURS = '24_hours'

class CreateQuoteRequestBodyQuoteType(str, Enum):
    r"""The type of the quote.
      * `balance_transfer`: Quote for transferring the balance from one currency to another within the same customer wallet.
      * `payout`: Quote for transferring money to a registered beneficiary's wallet in another currency.
    """
    BALANCE_TRANSFER = 'balance_transfer'
    PAYOUT = 'payout'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateQuoteRequestBody:
    r"""quoteCreationRequest"""
    conversion_schedule: Optional[CreateQuoteRequestBodyConversionSchedule] = dataclasses.field(default=CreateQuoteRequestBodyConversionSchedule.IMMEDIATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conversionSchedule'), 'exclude': lambda f: f is None }})
    r"""The time period after which the conversion should be settled."""
    destination_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the destination amount."""
    lock_period: Optional[CreateQuoteRequestBodyLockPeriod] = dataclasses.field(default=CreateQuoteRequestBodyLockPeriod.FIVE_MINS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lockPeriod'), 'exclude': lambda f: f is None }})
    r"""The duration for which the quote remains valid after creation."""
    quote_type: Optional[CreateQuoteRequestBodyQuoteType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quoteType'), 'exclude': lambda f: f is None }})
    r"""The type of the quote.
      * `balance_transfer`: Quote for transferring the balance from one currency to another within the same customer wallet.
      * `payout`: Quote for transferring money to a registered beneficiary's wallet in another currency.
    """
    source_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the source amount."""
    



@dataclasses.dataclass
class CreateQuoteRequest:
    client_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientHashId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the client."""
    request_body: CreateQuoteRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""quoteCreationRequest"""
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-request-id', 'style': 'simple', 'explode': False }})
    r"""Enter a unique UUID value"""
    


class CreateQuoteQuoteCreationResponseConversionSchedule(str, Enum):
    r"""The time period after which the conversion should be settled."""
    IMMEDIATE = 'immediate'
    END_OF_DAY = 'end_of_day'
    NEXT_DAY = 'next_day'
    TWO_DAYS = '2_days'

class CreateQuoteQuoteCreationResponseLockPeriod(str, Enum):
    r"""The duration for which the quote remains valid after creation."""
    FIVE_MINS = '5_mins'
    FIFTEEN_MINS = '15_mins'
    ONE_HOUR = '1_hour'
    FOUR_HOURS = '4_hours'
    EIGHT_HOURS = '8_hours'
    TWENTY_FOUR_HOURS = '24_hours'

class CreateQuoteQuoteCreationResponseQuoteType(str, Enum):
    r"""The type of the quote.
      * `balance_transfer`: Quote for transferring the balance from one currency to another within the same customer wallet.
      * `payout`: Quote for transferring money to a registered beneficiary's wallet in another currency.
    """
    BALANCE_TRANSFER = 'balance_transfer'
    PAYOUT = 'payout'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateQuoteQuoteCreationResponse:
    r"""OK"""
    conversion_schedule: Optional[CreateQuoteQuoteCreationResponseConversionSchedule] = dataclasses.field(default=CreateQuoteQuoteCreationResponseConversionSchedule.IMMEDIATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conversionSchedule'), 'exclude': lambda f: f is None }})
    r"""The time period after which the conversion should be settled."""
    created_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Time of creation in UTC."""
    destination_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationAmount'), 'exclude': lambda f: f is None }})
    r"""The amount needed in the destination currency. This value is for reference only and will not be used as the actual conversion amount."""
    destination_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the destination amount."""
    destination_markup_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationMarkupAmount'), 'exclude': lambda f: f is None }})
    r"""The amount charged in the destination currency as the markup for the conversion."""
    ecb_exchange_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecbExchangeRate'), 'exclude': lambda f: f is None }})
    r"""Europe Central Bank's exchange rate for this currency pair, provided only for EU and UK."""
    exchange_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exchangeRate'), 'exclude': lambda f: f is None }})
    r"""Foreign exchange market rate for the currency pair, used as the benchmark for quote calculation."""
    expiry_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiryTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Expiry time of the quote in UTC."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the quote."""
    is_rate_stale: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRateStale'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the exchange rate provided is stale. A value of \\"true\\" suggests that the exchange rate information is no longer current. Clients can use this flag to make informed decisions based on the freshness of the exchange rate."""
    lock_period: Optional[CreateQuoteQuoteCreationResponseLockPeriod] = dataclasses.field(default=CreateQuoteQuoteCreationResponseLockPeriod.FIVE_MINS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lockPeriod'), 'exclude': lambda f: f is None }})
    r"""The duration for which the quote remains valid after creation."""
    markup_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markupRate'), 'exclude': lambda f: f is None }})
    r"""Markup rate applied to the exchange rate for the conversion by Nium."""
    net_exchange_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netExchangeRate'), 'exclude': lambda f: f is None }})
    r"""Exchange rate with markup to be used for the conversion."""
    quote_type: Optional[CreateQuoteQuoteCreationResponseQuoteType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quoteType'), 'exclude': lambda f: f is None }})
    r"""The type of the quote.
      * `balance_transfer`: Quote for transferring the balance from one currency to another within the same customer wallet.
      * `payout`: Quote for transferring money to a registered beneficiary's wallet in another currency.
    """
    rate_capture_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rateCaptureTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Time in UTC at which exchange rate was obtained from the rate provider"""
    source_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceAmount'), 'exclude': lambda f: f is None }})
    r"""The source amount to be converted to the destination currency. This value is for reference only and will not be used as the actual conversion amount."""
    source_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the source amount."""
    



@dataclasses.dataclass
class CreateQuoteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    quote_creation_response: Optional[CreateQuoteQuoteCreationResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

