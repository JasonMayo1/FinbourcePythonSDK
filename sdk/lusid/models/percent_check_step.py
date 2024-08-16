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

class PercentCheckStep(ComplianceStep):
    """
    PercentCheckStep
    """
    label: constr(strict=True, min_length=1) = Field(..., description="The label of the compliance step")
    limit_check_parameters: conlist(ComplianceTemplateParameter) = Field(..., alias="limitCheckParameters", description="Parameters required for an absolute limit check")
    warning_check_parameters: conlist(ComplianceTemplateParameter) = Field(..., alias="warningCheckParameters", description="Parameters required for a warning limit check")
    compliance_step_type: StrictStr = Field(..., alias="complianceStepType", description=". The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep")
    additional_properties: Dict[str, Any] = {}
    __properties = ["complianceStepType", "label", "limitCheckParameters", "warningCheckParameters"]

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
    def from_json(cls, json_str: str) -> PercentCheckStep:
        """Create an instance of PercentCheckStep from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in limit_check_parameters (list)
        _items = []
        if self.limit_check_parameters:
            for _item in self.limit_check_parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['limitCheckParameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warning_check_parameters (list)
        _items = []
        if self.warning_check_parameters:
            for _item in self.warning_check_parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warningCheckParameters'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PercentCheckStep:
        """Create an instance of PercentCheckStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PercentCheckStep.parse_obj(obj)

        _obj = PercentCheckStep.parse_obj({
            "compliance_step_type": obj.get("complianceStepType"),
            "label": obj.get("label"),
            "limit_check_parameters": [ComplianceTemplateParameter.from_dict(_item) for _item in obj.get("limitCheckParameters")] if obj.get("limitCheckParameters") is not None else None,
            "warning_check_parameters": [ComplianceTemplateParameter.from_dict(_item) for _item in obj.get("warningCheckParameters")] if obj.get("warningCheckParameters") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
