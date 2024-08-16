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
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from lusid.models.instrument_event_configuration import InstrumentEventConfiguration
from lusid.models.link import Link
from lusid.models.model_property import ModelProperty
from lusid.models.relationship import Relationship
from lusid.models.resource_id import ResourceId
from lusid.models.staged_modifications_info import StagedModificationsInfo
from lusid.models.version import Version

class Portfolio(BaseModel):
    """
    A list of portfolios.  # noqa: E501
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    id: ResourceId = Field(...)
    type: StrictStr = Field(..., description="The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction")
    display_name: constr(strict=True, min_length=1) = Field(..., alias="displayName", description="The name of the portfolio.")
    description: Optional[StrictStr] = Field(None, description="The long form description of the portfolio.")
    created: datetime = Field(..., description="The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.")
    parent_portfolio_id: Optional[ResourceId] = Field(None, alias="parentPortfolioId")
    version: Optional[Version] = None
    staged_modifications: Optional[StagedModificationsInfo] = Field(None, alias="stagedModifications")
    is_derived: Optional[StrictBool] = Field(None, alias="isDerived", description="Whether or not this is a derived portfolio.")
    base_currency: Optional[StrictStr] = Field(None, alias="baseCurrency", description="The base currency of the portfolio.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="The requested portfolio properties. These will be from the 'Portfolio' domain.")
    relationships: Optional[conlist(Relationship)] = Field(None, description="A set of relationships associated to the portfolio.")
    instrument_scopes: Optional[conlist(StrictStr)] = Field(None, alias="instrumentScopes", description="The instrument scope resolution strategy of this portfolio.")
    accounting_method: Optional[StrictStr] = Field(None, alias="accountingMethod", description=". The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency")
    amortisation_method: Optional[StrictStr] = Field(None, alias="amortisationMethod", description="The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate")
    transaction_type_scope: Optional[StrictStr] = Field(None, alias="transactionTypeScope", description="The scope of the transaction types.")
    cash_gain_loss_calculation_date: Optional[StrictStr] = Field(None, alias="cashGainLossCalculationDate", description="The scope of the transaction types.")
    instrument_event_configuration: Optional[InstrumentEventConfiguration] = Field(None, alias="instrumentEventConfiguration")
    amortisation_rule_set_id: Optional[ResourceId] = Field(None, alias="amortisationRuleSetId")
    links: Optional[conlist(Link)] = None
    __properties = ["href", "id", "type", "displayName", "description", "created", "parentPortfolioId", "version", "stagedModifications", "isDerived", "baseCurrency", "properties", "relationships", "instrumentScopes", "accountingMethod", "amortisationMethod", "transactionTypeScope", "cashGainLossCalculationDate", "instrumentEventConfiguration", "amortisationRuleSetId", "links"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Transaction', 'Reference', 'DerivedTransaction'):
            raise ValueError("must be one of enum values ('Transaction', 'Reference', 'DerivedTransaction')")
        return value

    @validator('accounting_method')
    def accounting_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Default', 'AverageCost', 'FirstInFirstOut', 'LastInFirstOut', 'HighestCostFirst', 'LowestCostFirst', 'ProRateByUnits', 'ProRateByCost', 'ProRateByCostPortfolioCurrency'):
            raise ValueError("must be one of enum values ('Default', 'AverageCost', 'FirstInFirstOut', 'LastInFirstOut', 'HighestCostFirst', 'LowestCostFirst', 'ProRateByUnits', 'ProRateByCost', 'ProRateByCostPortfolioCurrency')")
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
    def from_json(cls, json_str: str) -> Portfolio:
        """Create an instance of Portfolio from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
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
        # override the default output from pydantic by calling `to_dict()` of staged_modifications
        if self.staged_modifications:
            _dict['stagedModifications'] = self.staged_modifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in relationships (list)
        _items = []
        if self.relationships:
            for _item in self.relationships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relationships'] = _items
        # override the default output from pydantic by calling `to_dict()` of instrument_event_configuration
        if self.instrument_event_configuration:
            _dict['instrumentEventConfiguration'] = self.instrument_event_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amortisation_rule_set_id
        if self.amortisation_rule_set_id:
            _dict['amortisationRuleSetId'] = self.amortisation_rule_set_id.to_dict()
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

        # set to None if base_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.base_currency is None and "base_currency" in self.__fields_set__:
            _dict['baseCurrency'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if relationships (nullable) is None
        # and __fields_set__ contains the field
        if self.relationships is None and "relationships" in self.__fields_set__:
            _dict['relationships'] = None

        # set to None if instrument_scopes (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_scopes is None and "instrument_scopes" in self.__fields_set__:
            _dict['instrumentScopes'] = None

        # set to None if amortisation_method (nullable) is None
        # and __fields_set__ contains the field
        if self.amortisation_method is None and "amortisation_method" in self.__fields_set__:
            _dict['amortisationMethod'] = None

        # set to None if transaction_type_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction_type_scope is None and "transaction_type_scope" in self.__fields_set__:
            _dict['transactionTypeScope'] = None

        # set to None if cash_gain_loss_calculation_date (nullable) is None
        # and __fields_set__ contains the field
        if self.cash_gain_loss_calculation_date is None and "cash_gain_loss_calculation_date" in self.__fields_set__:
            _dict['cashGainLossCalculationDate'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Portfolio:
        """Create an instance of Portfolio from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Portfolio.parse_obj(obj)

        _obj = Portfolio.parse_obj({
            "href": obj.get("href"),
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "type": obj.get("type"),
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "created": obj.get("created"),
            "parent_portfolio_id": ResourceId.from_dict(obj.get("parentPortfolioId")) if obj.get("parentPortfolioId") is not None else None,
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "staged_modifications": StagedModificationsInfo.from_dict(obj.get("stagedModifications")) if obj.get("stagedModifications") is not None else None,
            "is_derived": obj.get("isDerived"),
            "base_currency": obj.get("baseCurrency"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "relationships": [Relationship.from_dict(_item) for _item in obj.get("relationships")] if obj.get("relationships") is not None else None,
            "instrument_scopes": obj.get("instrumentScopes"),
            "accounting_method": obj.get("accountingMethod"),
            "amortisation_method": obj.get("amortisationMethod"),
            "transaction_type_scope": obj.get("transactionTypeScope"),
            "cash_gain_loss_calculation_date": obj.get("cashGainLossCalculationDate"),
            "instrument_event_configuration": InstrumentEventConfiguration.from_dict(obj.get("instrumentEventConfiguration")) if obj.get("instrumentEventConfiguration") is not None else None,
            "amortisation_rule_set_id": ResourceId.from_dict(obj.get("amortisationRuleSetId")) if obj.get("amortisationRuleSetId") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
