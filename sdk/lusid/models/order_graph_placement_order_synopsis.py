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
from pydantic.v1 import BaseModel, Field, conlist
from lusid.models.order_graph_placement_order_detail import OrderGraphPlacementOrderDetail

class OrderGraphPlacementOrderSynopsis(BaseModel):
    """
    OrderGraphPlacementOrderSynopsis
    """
    details: conlist(OrderGraphPlacementOrderDetail) = Field(..., description="Identifiers for each order in the block.")
    __properties = ["details"]

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
    def from_json(cls, json_str: str) -> OrderGraphPlacementOrderSynopsis:
        """Create an instance of OrderGraphPlacementOrderSynopsis from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item in self.details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderGraphPlacementOrderSynopsis:
        """Create an instance of OrderGraphPlacementOrderSynopsis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderGraphPlacementOrderSynopsis.parse_obj(obj)

        _obj = OrderGraphPlacementOrderSynopsis.parse_obj({
            "details": [OrderGraphPlacementOrderDetail.from_dict(_item) for _item in obj.get("details")] if obj.get("details") is not None else None
        })
        return _obj
