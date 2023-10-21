"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..errors import errorcodes500 as errors_errorcodes500
from dataclasses_json import Undefined, dataclass_json
from nium_platform import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ErrorDetail500:
    r"""error details description"""
    code: Optional[errors_errorcodes500.ErrorCodes500] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""The detailed error code associated with HTTP status 500.
    * `fx_dependency_error`: Error happens when the service calls its dependencies.
    * `fx_uncategorized_error`: Service errors not categorized.
    """
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the error."""
    

