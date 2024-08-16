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
from pydantic.v1 import BaseModel, Field, StrictStr
from lusid.models.property_value import PropertyValue

class ModelProperty(BaseModel):
    """
    ModelProperty
    """
    key: StrictStr = Field(..., description="The key of the property. This takes the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or 'Transaction/strategy/quantsignal'.")
    value: Optional[PropertyValue] = None
    effective_from: Optional[datetime] = Field(None, alias="effectiveFrom", description="The effective datetime from which the property is valid.")
    effective_until: Optional[datetime] = Field(None, alias="effectiveUntil", description="The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveFrom' datetime of the property.")
    __properties = ["key", "value", "effectiveFrom", "effectiveUntil"]

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
    def from_json(cls, json_str: str) -> ModelProperty:
        """Create an instance of ModelProperty from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # set to None if effective_from (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_from is None and "effective_from" in self.__fields_set__:
            _dict['effectiveFrom'] = None

        # set to None if effective_until (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_until is None and "effective_until" in self.__fields_set__:
            _dict['effectiveUntil'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelProperty:
        """Create an instance of ModelProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelProperty.parse_obj(obj)

        _obj = ModelProperty.parse_obj({
            "key": obj.get("key"),
            "value": PropertyValue.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "effective_from": obj.get("effectiveFrom"),
            "effective_until": obj.get("effectiveUntil")
        })
        return _obj
