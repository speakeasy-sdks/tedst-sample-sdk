"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import exchangeratesgetresponse as shared_exchangeratesgetresponse
from ..shared import window as shared_window
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class AggregatedExchangeRatesSecurity:
    default: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'x-api-key' }})
    



@dataclasses.dataclass
class AggregatedExchangeRatesRequest:
    destination_currency_code: str = dataclasses.field(metadata={'query_param': { 'field_name': 'destinationCurrencyCode', 'style': 'form', 'explode': True }})
    r"""This field contains the 3-letter [currency-and-country-codes](https://docs.nium.com/apis/docs/currency-and-country-codes)."""
    source_currency_code: str = dataclasses.field(metadata={'query_param': { 'field_name': 'sourceCurrencyCode', 'style': 'form', 'explode': True }})
    r"""This field contains the 3-letter [currency-and-country-codes](https://docs.nium.com/apis/docs/currency-and-country-codes)."""
    csrf_token: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'csrf_token', 'style': 'simple', 'explode': False }})
    end: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end', 'style': 'form', 'explode': True }})
    r"""The end timestamp used to filter the aggregated time series. Must be in the format 'yyyy-mm-ddTHH:MM:SSZ'."""
    start: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start', 'style': 'form', 'explode': True }})
    r"""The start timestamp used to filter the aggregated time series. Must be in the format 'yyyy-mm-ddTHH:MM:SSZ'."""
    window: Optional[shared_window.Window] = dataclasses.field(default=shared_window.Window.ONE_DAY, metadata={'query_param': { 'field_name': 'window', 'style': 'form', 'explode': True }})
    r"""Specifies the field by which the results should be grouped."""
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-request-id', 'style': 'simple', 'explode': False }})
    r"""Enter a unique UUID value."""
    



@dataclasses.dataclass
class AggregatedExchangeRatesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    exchange_rates_get_response: Optional[shared_exchangeratesgetresponse.ExchangeRatesGetResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

