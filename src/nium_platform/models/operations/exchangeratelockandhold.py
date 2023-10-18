"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import fxholdlockresponsecontent as shared_fxholdlockresponsecontent
from typing import Optional


@dataclasses.dataclass
class ExchangeRateLockandHoldSecurity:
    default: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'x-api-key' }})
    



@dataclasses.dataclass
class ExchangeRateLockandHoldRequest:
    client_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientHashId', 'style': 'simple', 'explode': False }})
    r"""Unique client identifier generated and shared before API handshake."""
    customer_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customerHashId', 'style': 'simple', 'explode': False }})
    r"""Unique customer identifier generated on customer creation."""
    destination_currency: str = dataclasses.field(metadata={'query_param': { 'field_name': 'destinationCurrency', 'style': 'form', 'explode': True }})
    r"""This field contains the [3-letter ISO-4217 currency code](doc:currency-and-country-codes) for the destination amount."""
    source_currency: str = dataclasses.field(metadata={'query_param': { 'field_name': 'sourceCurrency', 'style': 'form', 'explode': True }})
    r"""This field contains the [3-letter ISO-4217 currency code](doc:currency-and-country-codes) for the source amount."""
    wallet_hash_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'walletHashId', 'style': 'simple', 'explode': False }})
    r"""Unique wallet identifier generated simultaneously with customer creation."""
    additional_fx_markup: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'additionalFxMarkup', 'style': 'form', 'explode': True }})
    r"""This field is used if client wants to apply additional Fxmarkup in the exchange rate for their customer. The value should be in percentage. For example use 0.10 for 0.1% additional markup."""
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-request-id', 'style': 'simple', 'explode': False }})
    r"""Enter a unique UUID value"""
    



@dataclasses.dataclass
class ExchangeRateLockandHoldResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    fx_hold_lock_response_content: Optional[shared_fxholdlockresponsecontent.FxHoldLockResponseContent] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

