"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class QuoteType(str, Enum):
    r"""The type of the quote.
      * `balance_transfer`: Quote for transferring the balance from one currency to another within the same customer wallet.
      * `payout`: Quote for transferring money to a registered beneficiary's wallet in another currency.
    """
    BALANCE_TRANSFER = 'balance_transfer'
    PAYOUT = 'payout'
