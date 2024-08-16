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


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from lusid.models.composite_dispersion import CompositeDispersion
from lusid.models.link import Link

class CompositeDispersionResponse(BaseModel):
    """
    CompositeDispersionResponse
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    results: Optional[Dict[str, conlist(CompositeDispersion)]] = Field(None, description="Dispersion returns calculation grouped by ReturnId")
    links: Optional[conlist(Link)] = None
    __properties = ["href", "results", "links"]

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
    def from_json(cls, json_str: str) -> CompositeDispersionResponse:
        """Create an instance of CompositeDispersionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in results (dict of array)
        _field_dict_of_array = {}
        if self.results:
            for _key in self.results:
                if self.results[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.results[_key]
                    ]
            _dict['results'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if results (nullable) is None
        # and __fields_set__ contains the field
        if self.results is None and "results" in self.__fields_set__:
            _dict['results'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompositeDispersionResponse:
        """Create an instance of CompositeDispersionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompositeDispersionResponse.parse_obj(obj)

        _obj = CompositeDispersionResponse.parse_obj({
            "href": obj.get("href"),
            "results": dict(
                (_k,
                        [CompositeDispersion.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("results").items()
            ),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
