"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import conversioncreationresponse as shared_conversioncreationresponse
from typing import Optional


@dataclasses.dataclass
class FetchConversionRequest:
    client_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientHashId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the client."""
    conversion_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'conversionId', 'style': 'simple', 'explode': False }})
    customer_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customerHashId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the customer."""
    wallet_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'walletHashId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the wallet."""
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-request-id', 'style': 'simple', 'explode': False }})
    r"""Enter a unique UUID value"""
    



@dataclasses.dataclass
class FetchConversionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    conversion_creation_response: Optional[shared_conversioncreationresponse.ConversionCreationResponse] = dataclasses.field(default=None)
    r"""OK"""
    

