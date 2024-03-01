"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from nium_platform import utils
from nium_platform._hooks import HookContext
from nium_platform.models import errors, operations, shared
from typing import Optional

class Rates:
    r"""The Rates API"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def exchange_rate_v2(self, request: operations.ExchangeRateV2Request, security: operations.ExchangeRateV2Security) -> operations.ExchangeRateV2Response:
        r"""Exchange Rate V2
        This API fetches the interbank FX rate for a currency pair. Note that the rate provided does not include the Nium markup.
        """
        hook_ctx = HookContext(operation_id='ExchangeRateV2', oauth2_scopes=[], security_source=security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/v2/exchangeRate'
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ExchangeRateV2Request, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['401','403','404','4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ExchangeRateV2Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ExchangeRateV2ResponseDto])
                res.exchange_rate_v2_response_dto = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code == 403 or http_res.status_code == 404 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def aggregated_exchange_rates(self, request: operations.AggregatedExchangeRatesRequest, security: operations.AggregatedExchangeRatesSecurity) -> operations.AggregatedExchangeRatesResponse:
        r"""Fetch historic aggregated exchange rates
        This API will retrieve aggregated time series of historical exchange rate.
        """
        hook_ctx = HookContext(operation_id='aggregatedExchangeRates', oauth2_scopes=[], security_source=security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/v1/exchangeRates/aggregate'
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.AggregatedExchangeRatesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','401','403','4XX','500','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.AggregatedExchangeRatesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ExchangeRatesGetResponse])
                res.exchange_rates_get_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorResponse400)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorResponse401)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorResponse403)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.ErrorResponse500)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    