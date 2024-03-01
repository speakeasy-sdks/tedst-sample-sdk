"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .conversions import Conversions
from .conversions_previous_version_ import ConversionsPreviousVersion
from .quotes import Quotes
from .quotes_previous_version_ import QuotesPreviousVersion
from .rates import Rates
from .sdkconfiguration import SDKConfiguration
from nium_platform import utils
from nium_platform._hooks import SDKHooks
from nium_platform.models import shared
from typing import Callable, Dict, Union

class NIUMPlatform:
    r"""NIUM Platform: NIUM Platform"""
    conversions: Conversions
    r"""The Conversions API"""
    quotes_previous_version: QuotesPreviousVersion
    r"""The previous version of the Quotes API"""
    conversions_previous_version: ConversionsPreviousVersion
    r"""The Previous version of the Conversions API"""
    quotes: Quotes
    r"""The Quotes API"""
    rates: Rates
    r"""The Rates API"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 default: Union[str, Callable[[], str]],
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param default: The default required for authentication
        :type default: Union[str, Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if callable(default):
            def security():
                return shared.Security(default = default())
        else:
            security = shared.Security(default = default)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks=hooks
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.conversions = Conversions(self.sdk_configuration)
        self.quotes_previous_version = QuotesPreviousVersion(self.sdk_configuration)
        self.conversions_previous_version = ConversionsPreviousVersion(self.sdk_configuration)
        self.quotes = Quotes(self.sdk_configuration)
        self.rates = Rates(self.sdk_configuration)
    