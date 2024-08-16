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
from pydantic.v1 import BaseModel, Field, constr, validator
from lusid.models.aggregation_context import AggregationContext
from lusid.models.holding_context import HoldingContext
from lusid.models.market_context import MarketContext
from lusid.models.pricing_context import PricingContext
from lusid.models.translation_context import TranslationContext

class ConfigurationRecipe(BaseModel):
    """
    The Configuration or Calculation Recipe controls how LUSID processes a given request.  This can be used to change where market data used in pricing is loaded from and in what order, or which model is used to  price a given instrument as well as how aggregation will process the produced results.  # noqa: E501
    """
    scope: constr(strict=True, max_length=64, min_length=1) = Field(..., description="The scope used when updating or inserting the Configuration Recipe.")
    code: constr(strict=True, max_length=64, min_length=1) = Field(..., description="User given string name (code) to identify the recipe.")
    market: Optional[MarketContext] = None
    pricing: Optional[PricingContext] = None
    aggregation: Optional[AggregationContext] = None
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="User can assign a description to understand more humanly the recipe.")
    holding: Optional[HoldingContext] = None
    translation: Optional[TranslationContext] = None
    __properties = ["scope", "code", "market", "pricing", "aggregation", "description", "holding", "translation"]

    @validator('scope')
    def scope_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
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
    def from_json(cls, json_str: str) -> ConfigurationRecipe:
        """Create an instance of ConfigurationRecipe from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of market
        if self.market:
            _dict['market'] = self.market.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pricing
        if self.pricing:
            _dict['pricing'] = self.pricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aggregation
        if self.aggregation:
            _dict['aggregation'] = self.aggregation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of holding
        if self.holding:
            _dict['holding'] = self.holding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of translation
        if self.translation:
            _dict['translation'] = self.translation.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigurationRecipe:
        """Create an instance of ConfigurationRecipe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigurationRecipe.parse_obj(obj)

        _obj = ConfigurationRecipe.parse_obj({
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "market": MarketContext.from_dict(obj.get("market")) if obj.get("market") is not None else None,
            "pricing": PricingContext.from_dict(obj.get("pricing")) if obj.get("pricing") is not None else None,
            "aggregation": AggregationContext.from_dict(obj.get("aggregation")) if obj.get("aggregation") is not None else None,
            "description": obj.get("description"),
            "holding": HoldingContext.from_dict(obj.get("holding")) if obj.get("holding") is not None else None,
            "translation": TranslationContext.from_dict(obj.get("translation")) if obj.get("translation") is not None else None
        })
        return _obj
