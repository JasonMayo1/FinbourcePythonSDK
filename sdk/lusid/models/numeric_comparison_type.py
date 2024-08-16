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





class NumericComparisonType(str, Enum):
    """
    Comparison types for numerical data
    """

    """
    allowed enum values
    """
    EXACT = 'Exact'
    ABSOLUTEDIFFERENCE = 'AbsoluteDifference'
    RELATIVEDIFFERENCE = 'RelativeDifference'

    @classmethod
    def from_json(cls, json_str: str) -> NumericComparisonType:
        """Create an instance of NumericComparisonType from a JSON string"""
        return NumericComparisonType(json.loads(json_str))
