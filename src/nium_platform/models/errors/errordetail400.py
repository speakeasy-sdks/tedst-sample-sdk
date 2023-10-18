"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..errors import errorcodes400 as errors_errorcodes400
from dataclasses_json import Undefined, dataclass_json
from nium_platform import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ErrorDetail400(Exception):
    r"""error details description"""
    code: Optional[errors_errorcodes400.ErrorCodes400] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""The detailed error code associated with HTTP status 400.

    * `fx_constraint_violated_input`: The input violates the model constraints.
    * `fx_invalid_format_input`: The input format is invalid.
    * `fx_invalid_currency_code`: The input currency code is invalid.
    * `fx_missing_input`: The required fields are missing.
    * `fx_date_range_invalid`: The date range should be within 90 days.
    """
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the error."""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
