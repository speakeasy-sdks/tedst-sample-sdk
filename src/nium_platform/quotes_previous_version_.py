"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from nium_platform import utils
from nium_platform.models import errors, operations, shared
from typing import Optional

class QuotesPreviousVersion:
    r"""The previous version of the Quotes API"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def exchange_rate_lockand_hold(self, request: operations.ExchangeRateLockandHoldRequest, security: operations.ExchangeRateLockandHoldSecurity) -> operations.ExchangeRateLockandHoldResponse:
        r"""Exchange Rate Lock and Hold
        This API allows you to fetch exchange rate, and lock and hold the rates till a certain amount of time.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ExchangeRateLockandHoldRequest, base_url, '/api/v1/client/{clientHashId}/customer/{customerHashId}/wallet/{walletHashId}/lockExchangeRate', request)
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ExchangeRateLockandHoldRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ExchangeRateLockandHoldResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FxHoldLockResponseContent])
                res.fx_hold_lock_response_content = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.WalletAPIError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code == 403 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def exchange_rate_with_markup(self, request: operations.ExchangeRateWithMarkupRequest, security: operations.ExchangeRateWithMarkupSecurity) -> operations.ExchangeRateWithMarkupResponse:
        r"""Exchange Rate With Markup
        This API fetches the exchange rate between source currency and destination currency. If either source or destination amount is provided, the equivalent amount will also be returned. Note that you may not send both sourceAmount and destinationAmount as query parameters together. If both are provided, sourceAmount shall be taken for conversion.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ExchangeRateWithMarkupRequest, base_url, '/api/v1/client/{clientHashId}/exchangeRate', request)
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ExchangeRateWithMarkupRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ExchangeRateWithMarkupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ExchangeRateWithMarkupExchangeRateV2ResponseDto])
                res.exchange_rate_v2_response_dto = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code == 403 or http_res.status_code == 404 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    