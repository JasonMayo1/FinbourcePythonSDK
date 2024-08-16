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


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, constr

class LineageMember(BaseModel):
    """
    LineageMember
    """
    index: StrictInt = Field(..., description="Index to demonstrate position of lineage member in overall lineage")
    label: constr(strict=True, max_length=6000, min_length=0) = Field(..., description="Label of the step corresponding to this lineage member")
    sub_label: constr(strict=True, max_length=6000, min_length=0) = Field(..., alias="subLabel", description="SubLabel of the step corresponding to this lineage member")
    info_type: Optional[constr(strict=True, max_length=6000, min_length=0)] = Field(None, alias="infoType", description="Optional. Type of Information")
    information: Optional[constr(strict=True, max_length=6000, min_length=0)] = Field(None, description="Optional. Information for the step corresponding to this lineage member, of type InfoType")
    __properties = ["index", "label", "subLabel", "infoType", "information"]

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
    def from_json(cls, json_str: str) -> LineageMember:
        """Create an instance of LineageMember from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if info_type (nullable) is None
        # and __fields_set__ contains the field
        if self.info_type is None and "info_type" in self.__fields_set__:
            _dict['infoType'] = None

        # set to None if information (nullable) is None
        # and __fields_set__ contains the field
        if self.information is None and "information" in self.__fields_set__:
            _dict['information'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LineageMember:
        """Create an instance of LineageMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LineageMember.parse_obj(obj)

        _obj = LineageMember.parse_obj({
            "index": obj.get("index"),
            "label": obj.get("label"),
            "sub_label": obj.get("subLabel"),
            "info_type": obj.get("infoType"),
            "information": obj.get("information")
        })
        return _obj
