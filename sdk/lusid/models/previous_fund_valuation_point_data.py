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
from pydantic.v1 import BaseModel, Field
from lusid.models.fund_previous_nav import FundPreviousNAV
from lusid.models.unitisation_data import UnitisationData

class PreviousFundValuationPointData(BaseModel):
    """
    The data for a Fund at the previous valuation point.  # noqa: E501
    """
    nav: FundPreviousNAV = Field(...)
    unitisation: Optional[UnitisationData] = None
    __properties = ["nav", "unitisation"]

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
    def from_json(cls, json_str: str) -> PreviousFundValuationPointData:
        """Create an instance of PreviousFundValuationPointData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of nav
        if self.nav:
            _dict['nav'] = self.nav.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unitisation
        if self.unitisation:
            _dict['unitisation'] = self.unitisation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PreviousFundValuationPointData:
        """Create an instance of PreviousFundValuationPointData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PreviousFundValuationPointData.parse_obj(obj)

        _obj = PreviousFundValuationPointData.parse_obj({
            "nav": FundPreviousNAV.from_dict(obj.get("nav")) if obj.get("nav") is not None else None,
            "unitisation": UnitisationData.from_dict(obj.get("unitisation")) if obj.get("unitisation") is not None else None
        })
        return _obj
