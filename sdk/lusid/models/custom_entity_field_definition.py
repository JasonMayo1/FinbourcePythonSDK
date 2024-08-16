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
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr

class CustomEntityFieldDefinition(BaseModel):
    """
    CustomEntityFieldDefinition
    """
    name: constr(strict=True, min_length=1) = Field(..., description="The name of the field.")
    lifetime: constr(strict=True, min_length=1) = Field(..., description="Describes how the field’s values can change over time. The available values are: “Perpetual”, “TimeVariant”.")
    type: constr(strict=True, min_length=1) = Field(..., description="The value type for the field. Available values are: “String”, “Boolean”, “DateTime”, “Decimal”.")
    collection_type: Optional[StrictStr] = Field(None, alias="collectionType", description="The collection type for the field. Available values are: “Single”, “Array”. Null value defaults to “Single”")
    required: StrictBool = Field(..., description="Whether the field is required or not.")
    description: Optional[constr(strict=True, max_length=512)] = Field(None, description="An optional description for the field.")
    __properties = ["name", "lifetime", "type", "collectionType", "required", "description"]

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
    def from_json(cls, json_str: str) -> CustomEntityFieldDefinition:
        """Create an instance of CustomEntityFieldDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if collection_type (nullable) is None
        # and __fields_set__ contains the field
        if self.collection_type is None and "collection_type" in self.__fields_set__:
            _dict['collectionType'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomEntityFieldDefinition:
        """Create an instance of CustomEntityFieldDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomEntityFieldDefinition.parse_obj(obj)

        _obj = CustomEntityFieldDefinition.parse_obj({
            "name": obj.get("name"),
            "lifetime": obj.get("lifetime"),
            "type": obj.get("type"),
            "collection_type": obj.get("collectionType"),
            "required": obj.get("required"),
            "description": obj.get("description")
        })
        return _obj
