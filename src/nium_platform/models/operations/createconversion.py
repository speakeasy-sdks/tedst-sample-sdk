"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import conversioncreationrequest as shared_conversioncreationrequest
from ...models.shared import conversioncreationresponse as shared_conversioncreationresponse
from typing import Optional, Union


@dataclasses.dataclass
class CreateConversionSecurity:
    default: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'x-api-key' }})
    



@dataclasses.dataclass
class CreateConversionRequest:
    client_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientHashId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the client."""
    conversion_creation_request: Union[Union[shared_with_quote_id.ConversionCreationRequestSchemasWithSourceAmount, shared_with_quote_id.ConversionCreationRequestSchemasWithDestinationAmount], Union[shared_with_currency_pair.ConversionCreationRequestWithSourceAmount, shared_with_currency_pair.ConversionCreationRequestWithDestinationAmount]] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""ConversionCreationRequest"""
    customer_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customerHashId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the customer."""
    wallet_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'walletHashId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the wallet."""
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-request-id', 'style': 'simple', 'explode': False }})
    r"""Enter a unique UUID value"""
    



@dataclasses.dataclass
class CreateConversionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    conversion_creation_response: Optional[shared_conversioncreationresponse.ConversionCreationResponse] = dataclasses.field(default=None)
    r"""OK"""
    

