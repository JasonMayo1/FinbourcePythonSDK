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

from datetime import datetime
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

class LoanPeriod(BaseModel):
    """
    LoanPeriod
    """
    payment_date: datetime = Field(..., alias="paymentDate")
    notional: Union[StrictFloat, StrictInt] = Field(...)
    interest_amount: Union[StrictFloat, StrictInt] = Field(..., alias="interestAmount")
    __properties = ["paymentDate", "notional", "interestAmount"]

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
    def from_json(cls, json_str: str) -> LoanPeriod:
        """Create an instance of LoanPeriod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoanPeriod:
        """Create an instance of LoanPeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoanPeriod.parse_obj(obj)

        _obj = LoanPeriod.parse_obj({
            "payment_date": obj.get("paymentDate"),
            "notional": obj.get("notional"),
            "interest_amount": obj.get("interestAmount")
        })
        return _obj
