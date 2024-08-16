# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class QuoteType(str, Enum):
    """
    QuoteType
    """

    """
    allowed enum values
    """
    PRICE = 'Price'
    SPREAD = 'Spread'
    RATE = 'Rate'
    LOGNORMALVOL = 'LogNormalVol'
    NORMALVOL = 'NormalVol'
    PARSPREAD = 'ParSpread'
    ISDASPREAD = 'IsdaSpread'
    UPFRONT = 'Upfront'
    INDEX = 'Index'
    RATIO = 'Ratio'
    DELTA = 'Delta'
    POOLFACTOR = 'PoolFactor'
    INFLATIONASSUMPTION = 'InflationAssumption'
    DIRTYPRICE = 'DirtyPrice'
    PRINCIPALWRITEOFF = 'PrincipalWriteOff'
    INTERESTDEFERRED = 'InterestDeferred'
    INTERESTSHORTFALL = 'InterestShortfall'

    @classmethod
    def from_json(cls, json_str: str) -> QuoteType:
        """Create an instance of QuoteType from a JSON string"""
        return QuoteType(json.loads(json_str))
