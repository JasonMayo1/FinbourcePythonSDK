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
from pydantic.v1 import BaseModel, Field, conint

class DayMonth(BaseModel):
    """
    DayMonth
    """
    day: conint(strict=True, le=31, ge=1) = Field(..., description="Day part of Day, Month for Year End date specification.")
    month: conint(strict=True, le=12, ge=1) = Field(..., description="Month part of Day, Month for Year End date specification.")
    __properties = ["day", "month"]

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
    def from_json(cls, json_str: str) -> DayMonth:
        """Create an instance of DayMonth from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DayMonth:
        """Create an instance of DayMonth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DayMonth.parse_obj(obj)

        _obj = DayMonth.parse_obj({
            "day": obj.get("day"),
            "month": obj.get("month")
        })
        return _obj
