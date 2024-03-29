"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .cancellationreason import CancellationReason
from .conversionstatus import ConversionStatus
from dataclasses_json import Undefined, dataclass_json
from nium_platform import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConversionCancelResponse:
    cancellation_comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellationComment'), 'exclude': lambda f: f is None }})
    r"""Free text comment for clients to record and track cancellation of the conversion."""
    cancellation_fee: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellationFee'), 'exclude': lambda f: f is None }})
    r"""The fee charged when executing the cancellation."""
    cancellation_fee_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellationFeeCurrencyCode'), 'exclude': lambda f: f is None }})
    r"""3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the cancellation fee."""
    cancellation_fee_system_reference_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellationFeeSystemReferenceNumber'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for wallet financial activities used in all Nium reports and dashboards. Refer to [doc](https://docs.nium.com/apis/reference/clienttransactions) for details."""
    cancellation_reason: Optional[CancellationReason] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellationReason'), 'exclude': lambda f: f is None }})
    r"""Reason for a conversion cancellation.
      * `user_cancel`: User initiated cancellation.
      * `insufficient_fund`: Cancellation due to insufficient balance in the wallet at the time of conversion execution.
    """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the conversion."""
    status: Optional[ConversionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the conversion."""
    system_reference_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemReferenceNumber'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for wallet financial activities used in all Nium reports and dashboards. Refer to [doc](https://docs.nium.com/apis/reference/clienttransactions) for details."""
    

