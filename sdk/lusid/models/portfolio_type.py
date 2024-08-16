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





class PortfolioType(str, Enum):
    """
    PortfolioType
    """

    """
    allowed enum values
    """
    TRANSACTION = 'Transaction'
    REFERENCE = 'Reference'
    DERIVEDTRANSACTION = 'DerivedTransaction'

    @classmethod
    def from_json(cls, json_str: str) -> PortfolioType:
        """Create an instance of PortfolioType from a JSON string"""
        return PortfolioType(json.loads(json_str))
