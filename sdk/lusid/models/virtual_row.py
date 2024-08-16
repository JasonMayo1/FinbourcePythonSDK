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
from pydantic.v1 import BaseModel, Field, StrictStr
from lusid.models.result_value import ResultValue

class VirtualRow(BaseModel):
    """
    Rows identified by the composite id, based on the data maps  # noqa: E501
    """
    row_id: Optional[Dict[str, StrictStr]] = Field(None, alias="rowId", description="The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents.")
    row_data: Optional[Dict[str, ResultValue]] = Field(None, alias="rowData", description="The data for the particular row")
    __properties = ["rowId", "rowData"]

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
    def from_json(cls, json_str: str) -> VirtualRow:
        """Create an instance of VirtualRow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in row_data (dict)
        _field_dict = {}
        if self.row_data:
            for _key in self.row_data:
                if self.row_data[_key]:
                    _field_dict[_key] = self.row_data[_key].to_dict()
            _dict['rowData'] = _field_dict
        # set to None if row_id (nullable) is None
        # and __fields_set__ contains the field
        if self.row_id is None and "row_id" in self.__fields_set__:
            _dict['rowId'] = None

        # set to None if row_data (nullable) is None
        # and __fields_set__ contains the field
        if self.row_data is None and "row_data" in self.__fields_set__:
            _dict['rowData'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VirtualRow:
        """Create an instance of VirtualRow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VirtualRow.parse_obj(obj)

        _obj = VirtualRow.parse_obj({
            "row_id": obj.get("rowId"),
            "row_data": dict(
                (_k, ResultValue.from_dict(_v))
                for _k, _v in obj.get("rowData").items()
            )
            if obj.get("rowData") is not None
            else None
        })
        return _obj
