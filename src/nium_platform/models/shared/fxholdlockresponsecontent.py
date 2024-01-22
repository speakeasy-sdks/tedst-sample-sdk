"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from nium_platform import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FxHoldLockResponseContent:
    additional_fx_markup: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalFxMarkup'), 'exclude': lambda f: f is None }})
    r"""This field contains the Additional Fx Markup of the given audit ID"""
    audit_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audit_id'), 'exclude': lambda f: f is None }})
    r"""This field contains the audit ID which is generated by NIUM as a unique number for internal purpose."""
    destination_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination_currency'), 'exclude': lambda f: f is None }})
    r"""This field contains the 3-letter [ISO-4217 destination currency code](doc:currency-and-country-codes) for the destination amount."""
    ecb_fx_rate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecb_fx_rate'), 'exclude': lambda f: f is None }})
    r"""This field contains the ECB exchange rate."""
    fx_hold_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fx_hold_id'), 'exclude': lambda f: f is None }})
    r"""This field contains the foreign exchange hold ID."""
    fx_rate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fx_rate'), 'exclude': lambda f: f is None }})
    r"""This field contains the real time FX provider rate."""
    hold_expiry_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hold_expiry_at'), 'exclude': lambda f: f is None }})
    r"""This field contains the timestamp till which the exchange rate will be valid. In other words, the timestamp at which the exchange rate held by NIUM shall expire. Format of this field is yyyy-MM-ddTHH:mm:ss.SSSZ."""
    markup_rate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markup_rate'), 'exclude': lambda f: f is None }})
    r"""This field contains the markup rate charged by NIUM."""
    source_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_currency'), 'exclude': lambda f: f is None }})
    r"""This field contains the 3-letter [ISO-4217 source currency code](doc:currency-and-country-codes) for the source amount."""
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""This field contains the status of the given audit ID"""
    

