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
from pydantic.v1 import BaseModel, Field, constr
from lusid.models.model_property import ModelProperty

class UpsertPersonRequest(BaseModel):
    """
    UpsertPersonRequest
    """
    identifiers: Dict[str, ModelProperty] = Field(..., description="The identifiers the person will be upserted with.The provided keys should be idTypeScope, idTypeCode, code")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="A set of properties associated to the Person. There can be multiple properties associated with a property key.")
    display_name: constr(strict=True, max_length=512, min_length=1) = Field(..., alias="displayName", description="The display name of the Person")
    description: Optional[constr(strict=True, max_length=512, min_length=0)] = Field(None, description="The description of the Person")
    __properties = ["identifiers", "properties", "displayName", "description"]

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
    def from_json(cls, json_str: str) -> UpsertPersonRequest:
        """Create an instance of UpsertPersonRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in identifiers (dict)
        _field_dict = {}
        if self.identifiers:
            for _key in self.identifiers:
                if self.identifiers[_key]:
                    _field_dict[_key] = self.identifiers[_key].to_dict()
            _dict['identifiers'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpsertPersonRequest:
        """Create an instance of UpsertPersonRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpsertPersonRequest.parse_obj(obj)

        _obj = UpsertPersonRequest.parse_obj({
            "identifiers": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("identifiers").items()
            )
            if obj.get("identifiers") is not None
            else None,
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description")
        })
        return _obj
