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
from lusid.models.typed_resource_id import TypedResourceId

class CustodianAccountRequest(BaseModel):
    """
    CustodianAccountRequest
    """
    scope: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, description="The Scope assigned to the Custodian Account, where left blank the parent Portfolio Scope will be used")
    code: constr(strict=True, max_length=64, min_length=1) = Field(..., description="Unique Code representing the Custodian Account")
    status: Optional[StrictStr] = Field(None, description="The Account status. Can be Active, Inactive or Deleted.")
    account_number: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="accountNumber", description="The Custodian Account Number")
    account_name: constr(strict=True, max_length=512, min_length=1) = Field(..., alias="accountName", description="The identifiable name given to the Custodian Account")
    accounting_method: constr(strict=True, min_length=1) = Field(..., alias="accountingMethod", description="The Accounting method to be used")
    currency: StrictStr = Field(..., description="The Currency for the Account")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the 'CustodianAccount' domain.")
    custodian_identifier: TypedResourceId = Field(..., alias="custodianIdentifier")
    account_type: Optional[StrictStr] = Field(None, alias="accountType", description="The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin.")
    __properties = ["scope", "code", "status", "accountNumber", "accountName", "accountingMethod", "currency", "properties", "custodianIdentifier", "accountType"]

    @validator('scope')
    def scope_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('account_name')
    def account_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
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
    def from_json(cls, json_str: str) -> CustodianAccountRequest:
        """Create an instance of CustodianAccountRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custodian_identifier
        if self.custodian_identifier:
            _dict['custodianIdentifier'] = self.custodian_identifier.to_dict()
        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if account_type (nullable) is None
        # and __fields_set__ contains the field
        if self.account_type is None and "account_type" in self.__fields_set__:
            _dict['accountType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustodianAccountRequest:
        """Create an instance of CustodianAccountRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustodianAccountRequest.parse_obj(obj)

        _obj = CustodianAccountRequest.parse_obj({
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "status": obj.get("status"),
            "account_number": obj.get("accountNumber"),
            "account_name": obj.get("accountName"),
            "accounting_method": obj.get("accountingMethod"),
            "currency": obj.get("currency"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "custodian_identifier": TypedResourceId.from_dict(obj.get("custodianIdentifier")) if obj.get("custodianIdentifier") is not None else None,
            "account_type": obj.get("accountType")
        })
        return _obj
