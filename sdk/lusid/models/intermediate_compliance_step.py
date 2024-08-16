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
from pydantic.v1 import Field, StrictStr, conlist, constr, validator
from lusid.models.compliance_step import ComplianceStep
from lusid.models.compliance_template_parameter import ComplianceTemplateParameter

class IntermediateComplianceStep(ComplianceStep):
    """
    IntermediateComplianceStep
    """
    label: constr(strict=True, min_length=1) = Field(..., description="The label of the compliance step")
    grouped_parameters: Dict[str, conlist(ComplianceTemplateParameter)] = Field(..., alias="groupedParameters", description="Parameters required for the step")
    compliance_step_type: StrictStr = Field(..., alias="complianceStepType", description=". The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep")
    additional_properties: Dict[str, Any] = {}
    __properties = ["complianceStepType", "label", "groupedParameters"]

    @validator('compliance_step_type')
    def compliance_step_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('FilterStep', 'GroupByStep', 'GroupFilterStep', 'BranchStep', 'RecombineStep', 'CheckStep', 'PercentCheckStep'):
            raise ValueError("must be one of enum values ('FilterStep', 'GroupByStep', 'GroupFilterStep', 'BranchStep', 'RecombineStep', 'CheckStep', 'PercentCheckStep')")
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
    def from_json(cls, json_str: str) -> IntermediateComplianceStep:
        """Create an instance of IntermediateComplianceStep from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in grouped_parameters (dict of array)
        _field_dict_of_array = {}
        if self.grouped_parameters:
            for _key in self.grouped_parameters:
                if self.grouped_parameters[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.grouped_parameters[_key]
                    ]
            _dict['groupedParameters'] = _field_dict_of_array
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IntermediateComplianceStep:
        """Create an instance of IntermediateComplianceStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IntermediateComplianceStep.parse_obj(obj)

        _obj = IntermediateComplianceStep.parse_obj({
            "compliance_step_type": obj.get("complianceStepType"),
            "label": obj.get("label"),
            "grouped_parameters": dict(
                (_k,
                        [ComplianceTemplateParameter.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("groupedParameters").items()
            )
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
