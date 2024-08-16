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
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator
from lusid.models.model_property import ModelProperty

class Account(BaseModel):
    """
    An account  # noqa: E501
    """
    code: constr(strict=True, max_length=64, min_length=1) = Field(..., description="The code given for the Account.")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="A description for the Account.")
    type: constr(strict=True, min_length=1) = Field(..., description="The Account type. Can have the values: Asset/Liabilities/Income/Expense/Capital/Revenue.")
    status: StrictStr = Field(..., description="The Account status. Can be Active, Inactive or Deleted. The available values are: Active, Inactive, Deleted")
    control: Optional[StrictStr] = Field(None, description="This allows users to specify whether this a protected Account that prevents direct manual journal adjustment. Can have the values: System/ManualIt will default to “Manual”.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="A set of properties for the Account.")
    __properties = ["code", "description", "type", "status", "control", "properties"]

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Active', 'Inactive', 'Deleted'):
            raise ValueError("must be one of enum values ('Active', 'Inactive', 'Deleted')")
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
    def from_json(cls, json_str: str) -> Account:
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if control (nullable) is None
        # and __fields_set__ contains the field
        if self.control is None and "control" in self.__fields_set__:
            _dict['control'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Account:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Account.parse_obj(obj)

        _obj = Account.parse_obj({
            "code": obj.get("code"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "control": obj.get("control"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None
        })
        return _obj
