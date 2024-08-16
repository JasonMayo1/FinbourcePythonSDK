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





class ComplianceStepTypeRequest(str, Enum):
    """
    ComplianceStepTypeRequest
    """

    """
    allowed enum values
    """
    FILTERSTEPREQUEST = 'FilterStepRequest'
    GROUPBYSTEPREQUEST = 'GroupByStepRequest'
    GROUPFILTERSTEPREQUEST = 'GroupFilterStepRequest'
    BRANCHSTEPREQUEST = 'BranchStepRequest'
    CHECKSTEPREQUEST = 'CheckStepRequest'
    PERCENTCHECKSTEPREQUEST = 'PercentCheckStepRequest'

    @classmethod
    def from_json(cls, json_str: str) -> ComplianceStepTypeRequest:
        """Create an instance of ComplianceStepTypeRequest from a JSON string"""
        return ComplianceStepTypeRequest(json.loads(json_str))
