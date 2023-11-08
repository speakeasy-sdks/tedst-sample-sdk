"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from nium_platform import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConversionCreationRequestWithDestinationAmount:
    customer_comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerComment'), 'exclude': lambda f: f is None }})
    r"""Free text comment for clients to record and track the conversion."""
    destination_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationAmount'), 'exclude': lambda f: f is None }})
    r"""The amount needed in the destination currency."""
    destination_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the destination amount."""
    source_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the source amount."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConversionCreationRequestWithSourceAmount:
    customer_comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerComment'), 'exclude': lambda f: f is None }})
    r"""Free text comment for clients to record and track the conversion."""
    destination_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the destination amount."""
    source_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceAmount'), 'exclude': lambda f: f is None }})
    r"""The source amount to be converted to the destination currency."""
    source_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the source amount."""
    



@dataclasses.dataclass
class WithCurrencyPair:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConversionCreationRequestSchemasWithDestinationAmount:
    customer_comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerComment'), 'exclude': lambda f: f is None }})
    r"""Free text comment for clients to record and track the conversion."""
    destination_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationAmount'), 'exclude': lambda f: f is None }})
    r"""The amount needed in the destination currency."""
    quote_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quoteId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the quote."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConversionCreationRequestSchemasWithSourceAmount:
    customer_comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerComment'), 'exclude': lambda f: f is None }})
    r"""Free text comment for clients to record and track the conversion."""
    quote_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quoteId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the quote."""
    source_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceAmount'), 'exclude': lambda f: f is None }})
    r"""The source amount to be converted to the destination currency."""
    



@dataclasses.dataclass
class WithQuoteID:
    pass


@dataclasses.dataclass
class ConversionCreationRequest:
    pass
