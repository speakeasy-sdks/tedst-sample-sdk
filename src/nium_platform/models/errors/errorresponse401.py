"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.shared import errordetail401 as shared_errordetail401
from dataclasses_json import Undefined, dataclass_json
from nium_platform import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ErrorResponse401(Exception):
    r"""Error response when the request is unauthorized."""
    error_details: Optional[List[shared_errordetail401.ErrorDetail401]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorDetails'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
