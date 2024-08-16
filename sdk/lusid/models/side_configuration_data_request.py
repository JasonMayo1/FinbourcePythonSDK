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


from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

class SideConfigurationDataRequest(BaseModel):
    """
    Configuration needed to define a side. Sides are referenced by Label. Beyond that, other properties  can be used to reference either transaction fields, or transaction properties.  # noqa: E501
    """
    side: constr(strict=True, min_length=1) = Field(..., description="The side's label.")
    security: constr(strict=True, min_length=1) = Field(..., description="The security, or instrument.")
    currency: constr(strict=True, min_length=1) = Field(..., description="The currency.")
    rate: constr(strict=True, min_length=1) = Field(..., description="The rate.")
    units: constr(strict=True, min_length=1) = Field(..., description="The units.")
    amount: constr(strict=True, min_length=1) = Field(..., description="The amount.")
    __properties = ["side", "security", "currency", "rate", "units", "amount"]

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
    def from_json(cls, json_str: str) -> SideConfigurationDataRequest:
        """Create an instance of SideConfigurationDataRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SideConfigurationDataRequest:
        """Create an instance of SideConfigurationDataRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SideConfigurationDataRequest.parse_obj(obj)

        _obj = SideConfigurationDataRequest.parse_obj({
            "side": obj.get("side"),
            "security": obj.get("security"),
            "currency": obj.get("currency"),
            "rate": obj.get("rate"),
            "units": obj.get("units"),
            "amount": obj.get("amount")
        })
        return _obj
