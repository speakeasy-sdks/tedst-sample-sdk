"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from nium_platform import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExchangeRateV2ResponseDto:
    destination_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationAmount'), 'exclude': lambda f: f is None }})
    r"""The credited amount."""
    destination_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""This field contains the 3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the destination amount."""
    ecb_fx_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecbFxRate'), 'exclude': lambda f: f is None }})
    r"""The ecb exchange rate fetched for the conversion.
    This field is only applicable for EU and UK.
    """
    exchange_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exchangeRate'), 'exclude': lambda f: f is None }})
    r"""The exchange rate fetched for the conversion."""
    expiry_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiryDate'), 'exclude': lambda f: f is None }})
    r"""Timestamp till which the quoted rate is valid. The timezone is UTC +00."""
    markup_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markupAmount'), 'exclude': lambda f: f is None }})
    r"""In case source or destination amount is provided the markup amount will be calculated using markupRate."""
    markup_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markupRate'), 'exclude': lambda f: f is None }})
    r"""This is the markup rate charged by NIUM."""
    net_exchange_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netExchangeRate'), 'exclude': lambda f: f is None }})
    r"""This is exchangeRate subtracted by the markupRate."""
    quote_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quoteId'), 'exclude': lambda f: f is None }})
    r"""Unique quote Id for the exchange rate."""
    scaling_factor: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scalingFactor'), 'exclude': lambda f: f is None }})
    r"""The netExchangeRate should be divided by the scaling factor to fetch the actual exchange rate."""
    source_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceAmount'), 'exclude': lambda f: f is None }})
    r"""An amount to be converted."""
    source_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""This field contains the 3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the source amount."""
    
