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
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr, validator

class ShareClassDetails(BaseModel):
    """
    ShareClassDetails
    """
    lusid_instrument_id: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="lusidInstrumentId", description="LUSID's internal unique instrument identifier, resolved from the share class' instrument identifiers")
    instrument_scope: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="instrumentScope", description="The scope in which the share class instrument lies.")
    dom_currency: Optional[StrictStr] = Field(None, alias="domCurrency", description="The domestic currency of the share class instrument")
    instrument_active: Optional[StrictBool] = Field(None, alias="instrumentActive", description="If the instrument of the share class is active.")
    __properties = ["lusidInstrumentId", "instrumentScope", "domCurrency", "instrumentActive"]

    @validator('lusid_instrument_id')
    def lusid_instrument_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('instrument_scope')
    def instrument_scope_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
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
    def from_json(cls, json_str: str) -> ShareClassDetails:
        """Create an instance of ShareClassDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if lusid_instrument_id (nullable) is None
        # and __fields_set__ contains the field
        if self.lusid_instrument_id is None and "lusid_instrument_id" in self.__fields_set__:
            _dict['lusidInstrumentId'] = None

        # set to None if instrument_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_scope is None and "instrument_scope" in self.__fields_set__:
            _dict['instrumentScope'] = None

        # set to None if dom_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.dom_currency is None and "dom_currency" in self.__fields_set__:
            _dict['domCurrency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ShareClassDetails:
        """Create an instance of ShareClassDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ShareClassDetails.parse_obj(obj)

        _obj = ShareClassDetails.parse_obj({
            "lusid_instrument_id": obj.get("lusidInstrumentId"),
            "instrument_scope": obj.get("instrumentScope"),
            "dom_currency": obj.get("domCurrency"),
            "instrument_active": obj.get("instrumentActive")
        })
        return _obj
