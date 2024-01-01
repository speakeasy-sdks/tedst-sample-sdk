"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ConversionSchedule(str, Enum):
    r"""The time period after which the conversion should be settled."""
    IMMEDIATE = 'immediate'
    END_OF_DAY = 'end_of_day'
    NEXT_DAY = 'next_day'
    TWO_DAYS = '2_days'
