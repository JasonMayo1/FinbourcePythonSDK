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





class UnitSchema(str, Enum):
    """
    UnitSchema
    """

    """
    allowed enum values
    """
    NOUNITS = 'NoUnits'
    BASIC = 'Basic'
    ISO4217CURRENCY = 'Iso4217Currency'

    @classmethod
    def from_json(cls, json_str: str) -> UnitSchema:
        """Create an instance of UnitSchema from a JSON string"""
        return UnitSchema(json.loads(json_str))
