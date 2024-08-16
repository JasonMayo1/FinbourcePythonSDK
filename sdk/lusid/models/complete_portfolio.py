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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from lusid.models.link import Link
from lusid.models.model_property import ModelProperty
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class CompletePortfolio(BaseModel):
    """
    CompletePortfolio
    """
    id: ResourceId = Field(...)
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    description: Optional[StrictStr] = Field(None, description="The long form description of the portfolio.")
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="The name of the portfolio.")
    created: Optional[datetime] = Field(None, description="The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.")
    parent_portfolio_id: Optional[ResourceId] = Field(None, alias="parentPortfolioId")
    is_derived: Optional[StrictBool] = Field(None, alias="isDerived", description="Whether or not this is a derived portfolio.")
    type: Optional[StrictStr] = Field(None, description="The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction")
    version: Version = Field(...)
    properties: Optional[conlist(ModelProperty)] = Field(None, description="The requested portfolio properties. These will be from the 'Portfolio' domain.")
    base_currency: Optional[StrictStr] = Field(None, alias="baseCurrency", description="If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio.")
    sub_holding_keys: Optional[conlist(StrictStr)] = Field(None, alias="subHoldingKeys", description="The sub holding key properties configured for the portfolio")
    links: Optional[conlist(Link)] = None
    __properties = ["id", "href", "description", "displayName", "created", "parentPortfolioId", "isDerived", "type", "version", "properties", "baseCurrency", "subHoldingKeys", "links"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Transaction', 'Reference', 'DerivedTransaction'):
            raise ValueError("must be one of enum values ('Transaction', 'Reference', 'DerivedTransaction')")
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
    def from_json(cls, json_str: str) -> CompletePortfolio:
        """Create an instance of CompletePortfolio from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "is_derived",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_portfolio_id
        if self.parent_portfolio_id:
            _dict['parentPortfolioId'] = self.parent_portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item in self.properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['properties'] = _items
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

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if base_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.base_currency is None and "base_currency" in self.__fields_set__:
            _dict['baseCurrency'] = None

        # set to None if sub_holding_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.sub_holding_keys is None and "sub_holding_keys" in self.__fields_set__:
            _dict['subHoldingKeys'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompletePortfolio:
        """Create an instance of CompletePortfolio from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompletePortfolio.parse_obj(obj)

        _obj = CompletePortfolio.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "href": obj.get("href"),
            "description": obj.get("description"),
            "display_name": obj.get("displayName"),
            "created": obj.get("created"),
            "parent_portfolio_id": ResourceId.from_dict(obj.get("parentPortfolioId")) if obj.get("parentPortfolioId") is not None else None,
            "is_derived": obj.get("isDerived"),
            "type": obj.get("type"),
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "properties": [ModelProperty.from_dict(_item) for _item in obj.get("properties")] if obj.get("properties") is not None else None,
            "base_currency": obj.get("baseCurrency"),
            "sub_holding_keys": obj.get("subHoldingKeys"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
