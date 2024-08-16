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
from pydantic.v1 import BaseModel, constr

class TransactionCurrencyAndAmount(BaseModel):
    """
    TransactionCurrencyAndAmount
    """
    currency: Optional[constr(strict=True, max_length=1024, min_length=0)] = None
    amount: Optional[constr(strict=True, max_length=1024, min_length=0)] = None
    __properties = ["currency", "amount"]

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
    def from_json(cls, json_str: str) -> TransactionCurrencyAndAmount:
        """Create an instance of TransactionCurrencyAndAmount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionCurrencyAndAmount:
        """Create an instance of TransactionCurrencyAndAmount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionCurrencyAndAmount.parse_obj(obj)

        _obj = TransactionCurrencyAndAmount.parse_obj({
            "currency": obj.get("currency"),
            "amount": obj.get("amount")
        })
        return _obj
