"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from nium_platform import utils
from typing import List, Optional

class CancelConversion500ApplicationJSONErrorDetailsCode(str, Enum):
    r"""The detailed error code associated with HTTP status 500.
    * `fx_dependency_error`: Error happens when the service calls its dependencies.
    * `fx_uncategorized_error`: Service errors not categorized.
    """
    FX_DEPENDENCY_ERROR = 'fx_dependency_error'
    FX_UNCATEGORIZED_ERROR = 'fx_uncategorized_error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion500ApplicationJSONErrorDetails(Exception):
    r"""error details description"""
    code: Optional[CancelConversion500ApplicationJSONErrorDetailsCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""The detailed error code associated with HTTP status 500.
    * `fx_dependency_error`: Error happens when the service calls its dependencies.
    * `fx_uncategorized_error`: Service errors not categorized.
    """
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the error."""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion500ApplicationJSON(Exception):
    r"""Error response when service has internal error."""
    error_details: Optional[List[CancelConversion500ApplicationJSONErrorDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorDetails'), 'exclude': lambda f: f is None }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)

class CancelConversion404ApplicationJSONErrorDetailsCode(str, Enum):
    r"""The detailed error code associated with HTTP status 404.
    * `fx_quote_not_found`: The provided quote cannot be found in the service.
    * `fx_fee_configuration_not_found`: The configuration cannot be found for at least one of the fees.
    """
    FX_QUOTE_NOT_FOUND = 'fx_quote_not_found'
    FX_FEE_CONFIGURATION_NOT_FOUND = 'fx_fee_configuration_not_found'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion404ApplicationJSONErrorDetails(Exception):
    r"""error details description"""
    code: Optional[CancelConversion404ApplicationJSONErrorDetailsCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""The detailed error code associated with HTTP status 404.
    * `fx_quote_not_found`: The provided quote cannot be found in the service.
    * `fx_fee_configuration_not_found`: The configuration cannot be found for at least one of the fees.
    """
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the error."""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion404ApplicationJSON(Exception):
    r"""Error response when the requested resource cannot be found."""
    error_details: Optional[List[CancelConversion404ApplicationJSONErrorDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorDetails'), 'exclude': lambda f: f is None }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)

class CancelConversion403ApplicationJSONErrorDetailsCode(str, Enum):
    r"""The detailed error code associated with HTTP status 403.
    * `fx_client_no_access`: The client is authenticated but not authorized.
    """
    FX_CLIENT_NO_ACCESS = 'fx_client_no_access'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion403ApplicationJSONErrorDetails(Exception):
    r"""error details description"""
    code: Optional[CancelConversion403ApplicationJSONErrorDetailsCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""The detailed error code associated with HTTP status 403.
    * `fx_client_no_access`: The client is authenticated but not authorized.
    """
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the error."""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion403ApplicationJSON(Exception):
    r"""Error response when the requested resource is forbidden."""
    error_details: Optional[List[CancelConversion403ApplicationJSONErrorDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorDetails'), 'exclude': lambda f: f is None }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)

class CancelConversion401ApplicationJSONErrorDetailsCode(str, Enum):
    r"""The detailed error code associated with HTTP status 401.
    * `fx_client_unauthenticated`: The client request lacks valid authentication credentials.
    """
    FX_CLIENT_UNAUTHENTICATED = 'fx_client_unauthenticated'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion401ApplicationJSONErrorDetails(Exception):
    r"""error details description"""
    code: Optional[CancelConversion401ApplicationJSONErrorDetailsCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""The detailed error code associated with HTTP status 401.
    * `fx_client_unauthenticated`: The client request lacks valid authentication credentials.
    """
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the error."""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion401ApplicationJSON(Exception):
    r"""Error response when the request is unauthorized."""
    error_details: Optional[List[CancelConversion401ApplicationJSONErrorDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorDetails'), 'exclude': lambda f: f is None }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)

class CancelConversion400ApplicationJSONErrorDetailsCode(str, Enum):
    r"""The detailed error code associated with HTTP status 400.

    * `fx_constraint_violated_input`: The input violates the model constraints.
    * `fx_invalid_format_input`: The input format is invalid.
    * `fx_invalid_currency_code`: The input currency code is invalid.
    * `fx_invalid_currency_amount`: The input currency amount is invalid.
    * `fx_missing_input`: The required fields are missing.
    * `fx_quote_expired`: The provided quote is expired.
    * `fx_insufficient_balance`: The balance in the account is insufficient to complete/schedule the transfer.
    * `fx_transfer_status_invalid`: The transfer status is invalid.
    * `fx_locked_period`: The requested conversion is in locked period.
    """
    FX_CONSTRAINT_VIOLATED_INPUT = 'fx_constraint_violated_input'
    FX_INVALID_FORMAT_INPUT = 'fx_invalid_format_input'
    FX_INVALID_CURRENCY_CODE = 'fx_invalid_currency_code'
    FX_INVALID_CURRENCY_AMOUNT = 'fx_invalid_currency_amount'
    FX_MISSING_INPUT = 'fx_missing_input'
    FX_QUOTE_EXPIRED = 'fx_quote_expired'
    FX_INSUFFICIENT_BALANCE = 'fx_insufficient_balance'
    FX_TRANSFER_STATUS_INVALID = 'fx_transfer_status_invalid'
    FX_LOCKED_PERIOD = 'fx_locked_period'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion400ApplicationJSONErrorDetails(Exception):
    r"""error details description"""
    code: Optional[CancelConversion400ApplicationJSONErrorDetailsCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""The detailed error code associated with HTTP status 400.

    * `fx_constraint_violated_input`: The input violates the model constraints.
    * `fx_invalid_format_input`: The input format is invalid.
    * `fx_invalid_currency_code`: The input currency code is invalid.
    * `fx_invalid_currency_amount`: The input currency amount is invalid.
    * `fx_missing_input`: The required fields are missing.
    * `fx_quote_expired`: The provided quote is expired.
    * `fx_insufficient_balance`: The balance in the account is insufficient to complete/schedule the transfer.
    * `fx_transfer_status_invalid`: The transfer status is invalid.
    * `fx_locked_period`: The requested conversion is in locked period.
    """
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the error."""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CancelConversion400ApplicationJSON(Exception):
    r"""Error response when the request format is invalid."""
    error_details: Optional[List[CancelConversion400ApplicationJSONErrorDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorDetails'), 'exclude': lambda f: f is None }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
