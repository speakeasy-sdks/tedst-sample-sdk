"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import exchangeratev2responsedto as shared_exchangeratev2responsedto
from typing import Optional


@dataclasses.dataclass
class ExchangeRateWithMarkupSecurity:
    default: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'x-api-key' }})
    



@dataclasses.dataclass
class ExchangeRateWithMarkupRequest:
    client_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientHashId', 'style': 'simple', 'explode': False }})
    r"""Unique customer identifier generated on customer creation."""
    destination_currency_code: str = dataclasses.field(metadata={'query_param': { 'field_name': 'destinationCurrencyCode', 'style': 'form', 'explode': True }})
    r"""This field contains the 3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the destination amount."""
    source_currency_code: str = dataclasses.field(metadata={'query_param': { 'field_name': 'sourceCurrencyCode', 'style': 'form', 'explode': True }})
    r"""This field contains the 3-letter [ISO-4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) for the source amount."""
    destination_amount: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'destinationAmount', 'style': 'form', 'explode': True }})
    r"""An amount to which the source is converted. It can be used to find the necessary source amount value. If both sourceAmount and destinationAmount are provided, this field is ignored."""
    source_amount: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sourceAmount', 'style': 'form', 'explode': True }})
    r"""An amount to be converted. This field takes precedence over destinationAmount, in case both are provided."""
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-request-id', 'style': 'simple', 'explode': False }})
    r"""Enter a unique UUID value"""
    



@dataclasses.dataclass
class ExchangeRateWithMarkupResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    exchange_rate_v2_response_dto: Optional[shared_exchangeratev2responsedto.ExchangeRateV2ResponseDto] = dataclasses.field(default=None)
    r"""OK"""
    

