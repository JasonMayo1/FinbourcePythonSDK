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
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from lusid.models.instrument_event import InstrumentEvent
from lusid.models.new_instrument import NewInstrument
from lusid.models.units_ratio import UnitsRatio

class SpinOffEvent(InstrumentEvent):
    """
    Spin-off event (SOFF), representing the distribution of securities issued by another company.  # noqa: E501
    """
    announcement_date: Optional[datetime] = Field(None, alias="announcementDate", description="Optional.  The date the spin-off is announced.")
    ex_date: datetime = Field(..., alias="exDate", description="The first date on which the holder of record has entitled ownership of the new shares.")
    record_date: Optional[datetime] = Field(None, alias="recordDate", description="Optional.  Date you have to be the holder of record in order to receive the additional shares.")
    payment_date: datetime = Field(..., alias="paymentDate", description="Date on which the distribution of shares takes place.")
    new_instrument: NewInstrument = Field(..., alias="newInstrument")
    units_ratio: UnitsRatio = Field(..., alias="unitsRatio")
    cost_factor: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="costFactor", description="Optional. The fraction of cost that is transferred from the existing shares to the new shares.")
    fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="fractionalUnitsCashPrice", description="Optional. Used in calculating cash-in-lieu of fractional shares.")
    fractional_units_cash_currency: Optional[StrictStr] = Field(None, alias="fractionalUnitsCashCurrency", description="Optional. Used in calculating cash-in-lieu of fractional shares.")
    instrument_event_type: StrictStr = Field(..., alias="instrumentEventType", description="The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentEventType", "announcementDate", "exDate", "recordDate", "paymentDate", "newInstrument", "unitsRatio", "costFactor", "fractionalUnitsCashPrice", "fractionalUnitsCashCurrency"]

    @validator('instrument_event_type')
    def instrument_event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent', 'MergerEvent', 'FutureExpiryEvent'):
            raise ValueError("must be one of enum values ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent', 'MergerEvent', 'FutureExpiryEvent')")
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
    def from_json(cls, json_str: str) -> SpinOffEvent:
        """Create an instance of SpinOffEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of new_instrument
        if self.new_instrument:
            _dict['newInstrument'] = self.new_instrument.to_dict()
        # override the default output from pydantic by calling `to_dict()` of units_ratio
        if self.units_ratio:
            _dict['unitsRatio'] = self.units_ratio.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if announcement_date (nullable) is None
        # and __fields_set__ contains the field
        if self.announcement_date is None and "announcement_date" in self.__fields_set__:
            _dict['announcementDate'] = None

        # set to None if record_date (nullable) is None
        # and __fields_set__ contains the field
        if self.record_date is None and "record_date" in self.__fields_set__:
            _dict['recordDate'] = None

        # set to None if cost_factor (nullable) is None
        # and __fields_set__ contains the field
        if self.cost_factor is None and "cost_factor" in self.__fields_set__:
            _dict['costFactor'] = None

        # set to None if fractional_units_cash_price (nullable) is None
        # and __fields_set__ contains the field
        if self.fractional_units_cash_price is None and "fractional_units_cash_price" in self.__fields_set__:
            _dict['fractionalUnitsCashPrice'] = None

        # set to None if fractional_units_cash_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.fractional_units_cash_currency is None and "fractional_units_cash_currency" in self.__fields_set__:
            _dict['fractionalUnitsCashCurrency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpinOffEvent:
        """Create an instance of SpinOffEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpinOffEvent.parse_obj(obj)

        _obj = SpinOffEvent.parse_obj({
            "instrument_event_type": obj.get("instrumentEventType"),
            "announcement_date": obj.get("announcementDate"),
            "ex_date": obj.get("exDate"),
            "record_date": obj.get("recordDate"),
            "payment_date": obj.get("paymentDate"),
            "new_instrument": NewInstrument.from_dict(obj.get("newInstrument")) if obj.get("newInstrument") is not None else None,
            "units_ratio": UnitsRatio.from_dict(obj.get("unitsRatio")) if obj.get("unitsRatio") is not None else None,
            "cost_factor": obj.get("costFactor"),
            "fractional_units_cash_price": obj.get("fractionalUnitsCashPrice"),
            "fractional_units_cash_currency": obj.get("fractionalUnitsCashCurrency")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
