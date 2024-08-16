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


from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from lusid.models.aggregate_spec import AggregateSpec
from lusid.models.reconciliation_rule import ReconciliationRule

class ReconcileNumericRule(ReconciliationRule):
    """
    ReconcileNumericRule
    """
    comparison_type: StrictStr = Field(..., alias="comparisonType", description="The available values are: Exact, AbsoluteDifference, RelativeDifference")
    tolerance: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction.")
    applies_to: AggregateSpec = Field(..., alias="appliesTo")
    rule_type: StrictStr = Field(..., alias="ruleType", description="The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact")
    additional_properties: Dict[str, Any] = {}
    __properties = ["ruleType", "comparisonType", "tolerance", "appliesTo"]

    @validator('comparison_type')
    def comparison_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Exact', 'AbsoluteDifference', 'RelativeDifference'):
            raise ValueError("must be one of enum values ('Exact', 'AbsoluteDifference', 'RelativeDifference')")
        return value

    @validator('rule_type')
    def rule_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ReconcileNumericRule', 'ReconcileDateTimeRule', 'ReconcileStringRule', 'ReconcileExact'):
            raise ValueError("must be one of enum values ('ReconcileNumericRule', 'ReconcileDateTimeRule', 'ReconcileStringRule', 'ReconcileExact')")
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
    def from_json(cls, json_str: str) -> ReconcileNumericRule:
        """Create an instance of ReconcileNumericRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of applies_to
        if self.applies_to:
            _dict['appliesTo'] = self.applies_to.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReconcileNumericRule:
        """Create an instance of ReconcileNumericRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReconcileNumericRule.parse_obj(obj)

        _obj = ReconcileNumericRule.parse_obj({
            "rule_type": obj.get("ruleType"),
            "comparison_type": obj.get("comparisonType"),
            "tolerance": obj.get("tolerance"),
            "applies_to": AggregateSpec.from_dict(obj.get("appliesTo")) if obj.get("appliesTo") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
