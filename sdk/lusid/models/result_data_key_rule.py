# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictStr, constr, validator
from lusid.models.result_key_rule import ResultKeyRule

class ResultDataKeyRule(ResultKeyRule):
    """
    ResultDataKeyRule
    """
    supplier: constr(strict=True, max_length=32, min_length=0) = Field(..., description="the result resource supplier (where the data comes from)")
    data_scope: constr(strict=True, max_length=256, min_length=1) = Field(..., alias="dataScope", description="which is the scope in which the data should be found")
    document_code: constr(strict=True, max_length=256, min_length=1) = Field(..., alias="documentCode", description="document code that defines which document is desired")
    quote_interval: Optional[constr(strict=True, max_length=16, min_length=0)] = Field(None, alias="quoteInterval", description="Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago).")
    as_at: Optional[datetime] = Field(None, alias="asAt", description="The AsAt predicate specification.")
    resource_key: constr(strict=True, max_length=256, min_length=0) = Field(..., alias="resourceKey", description="The result data key that identifies the address pattern that this is a rule for")
    document_result_type: constr(strict=True, min_length=1) = Field(..., alias="documentResultType")
    result_key_rule_type: StrictStr = Field(..., alias="resultKeyRuleType", description="The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule")
    additional_properties: Dict[str, Any] = {}
    __properties = ["resultKeyRuleType", "supplier", "dataScope", "documentCode", "quoteInterval", "asAt", "resourceKey", "documentResultType"]

    @validator('data_scope')
    def data_scope_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('result_key_rule_type')
    def result_key_rule_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Invalid', 'ResultDataKeyRule', 'PortfolioResultDataKeyRule'):
            raise ValueError("must be one of enum values ('Invalid', 'ResultDataKeyRule', 'PortfolioResultDataKeyRule')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ResultDataKeyRule:
        """Create an instance of ResultDataKeyRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if quote_interval (nullable) is None
        # and __fields_set__ contains the field
        if self.quote_interval is None and "quote_interval" in self.__fields_set__:
            _dict['quoteInterval'] = None

        # set to None if as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at is None and "as_at" in self.__fields_set__:
            _dict['asAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResultDataKeyRule:
        """Create an instance of ResultDataKeyRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResultDataKeyRule.parse_obj(obj)

        _obj = ResultDataKeyRule.parse_obj({
            "result_key_rule_type": obj.get("resultKeyRuleType"),
            "supplier": obj.get("supplier"),
            "data_scope": obj.get("dataScope"),
            "document_code": obj.get("documentCode"),
            "quote_interval": obj.get("quoteInterval"),
            "as_at": obj.get("asAt"),
            "resource_key": obj.get("resourceKey"),
            "document_result_type": obj.get("documentResultType")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
