"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from nium_platform import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletTransferResponseDto:
    destination_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationAmount'), 'exclude': lambda f: f is None }})
    r"""Destination amount is the actual amount credited after deducting Fx and markup."""
    destination_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""This field contains the 3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the destination amount."""
    exchange_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exchangeRate'), 'exclude': lambda f: f is None }})
    r"""Exchange rate between source and destination currencies."""
    markup_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markupAmount'), 'exclude': lambda f: f is None }})
    r"""Markup amount calculated on the transaction."""
    markup_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markupRate'), 'exclude': lambda f: f is None }})
    r"""Cross-currency markup percentage levied by NIUM."""
    net_exchange_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netExchangeRate'), 'exclude': lambda f: f is None }})
    r"""Exchange rate between source and destination currencies derived after accounting for markup. The netExchangeRate should be divided by the scaling factor to fetch the actual exchange rate."""
    scaling_factor: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scalingFactor'), 'exclude': lambda f: f is None }})
    r"""The netExchangeRate should be divided by the scaling factor to fetch the actual exchange rate."""
    source_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceAmount'), 'exclude': lambda f: f is None }})
    r"""Source amount is the amount transferred by the customer."""
    source_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""This field contains the 3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the source amount."""
    system_reference_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemReferenceNumber'), 'exclude': lambda f: f is None }})
    r"""Unique auth code generated for the transaction by the card issuance platform."""
    

