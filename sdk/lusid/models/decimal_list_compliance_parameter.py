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
from pydantic.v1 import Field, StrictStr, validator
from lusid.models.compliance_parameter import ComplianceParameter
from lusid.models.resource_id import ResourceId

class DecimalListComplianceParameter(ComplianceParameter):
    """
    DecimalListComplianceParameter
    """
    value: ResourceId = Field(...)
    compliance_parameter_type: StrictStr = Field(..., alias="complianceParameterType", description="The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter")
    additional_properties: Dict[str, Any] = {}
    __properties = ["complianceParameterType", "value"]

    @validator('compliance_parameter_type')
    def compliance_parameter_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('BoolComplianceParameter', 'StringComplianceParameter', 'DecimalComplianceParameter', 'DateTimeComplianceParameter', 'PropertyKeyComplianceParameter', 'AddressKeyComplianceParameter', 'PortfolioIdComplianceParameter', 'PortfolioGroupIdComplianceParameter', 'StringListComplianceParameter', 'BoolListComplianceParameter', 'DateTimeListComplianceParameter', 'DecimalListComplianceParameter', 'PropertyKeyListComplianceParameter', 'AddressKeyListComplianceParameter', 'PortfolioIdListComplianceParameter', 'PortfolioGroupIdListComplianceParameter', 'InstrumentListComplianceParameter', 'FilterPredicateComplianceParameter', 'GroupFilterPredicateComplianceParameter', 'GroupBySelectorComplianceParameter', 'PropertyListComplianceParameter', 'GroupCalculationComplianceParameter'):
            raise ValueError("must be one of enum values ('BoolComplianceParameter', 'StringComplianceParameter', 'DecimalComplianceParameter', 'DateTimeComplianceParameter', 'PropertyKeyComplianceParameter', 'AddressKeyComplianceParameter', 'PortfolioIdComplianceParameter', 'PortfolioGroupIdComplianceParameter', 'StringListComplianceParameter', 'BoolListComplianceParameter', 'DateTimeListComplianceParameter', 'DecimalListComplianceParameter', 'PropertyKeyListComplianceParameter', 'AddressKeyListComplianceParameter', 'PortfolioIdListComplianceParameter', 'PortfolioGroupIdListComplianceParameter', 'InstrumentListComplianceParameter', 'FilterPredicateComplianceParameter', 'GroupFilterPredicateComplianceParameter', 'GroupBySelectorComplianceParameter', 'PropertyListComplianceParameter', 'GroupCalculationComplianceParameter')")
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
    def from_json(cls, json_str: str) -> DecimalListComplianceParameter:
        """Create an instance of DecimalListComplianceParameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DecimalListComplianceParameter:
        """Create an instance of DecimalListComplianceParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DecimalListComplianceParameter.parse_obj(obj)

        _obj = DecimalListComplianceParameter.parse_obj({
            "compliance_parameter_type": obj.get("complianceParameterType"),
            "value": ResourceId.from_dict(obj.get("value")) if obj.get("value") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
