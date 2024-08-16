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


from typing import Any, Dict, List
from pydantic.v1 import Field, StrictStr, conlist, validator
from lusid.models.economic_dependency import EconomicDependency

class CalendarDependency(EconomicDependency):
    """
    For indicating a dependency upon calendar codes  # noqa: E501
    """
    calendars: conlist(StrictStr) = Field(..., description="The Codes of the calendars that are depended upon.")
    dependency_type: StrictStr = Field(..., alias="dependencyType", description="The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency")
    additional_properties: Dict[str, Any] = {}
    __properties = ["dependencyType", "calendars"]

    @validator('dependency_type')
    def dependency_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('OpaqueDependency', 'CashDependency', 'DiscountingDependency', 'EquityCurveDependency', 'EquityVolDependency', 'FxDependency', 'FxForwardsDependency', 'FxVolDependency', 'IndexProjectionDependency', 'IrVolDependency', 'QuoteDependency', 'Vendor', 'CalendarDependency', 'InflationFixingDependency'):
            raise ValueError("must be one of enum values ('OpaqueDependency', 'CashDependency', 'DiscountingDependency', 'EquityCurveDependency', 'EquityVolDependency', 'FxDependency', 'FxForwardsDependency', 'FxVolDependency', 'IndexProjectionDependency', 'IrVolDependency', 'QuoteDependency', 'Vendor', 'CalendarDependency', 'InflationFixingDependency')")
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
    def from_json(cls, json_str: str) -> CalendarDependency:
        """Create an instance of CalendarDependency from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CalendarDependency:
        """Create an instance of CalendarDependency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CalendarDependency.parse_obj(obj)

        _obj = CalendarDependency.parse_obj({
            "dependency_type": obj.get("dependencyType"),
            "calendars": obj.get("calendars")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
