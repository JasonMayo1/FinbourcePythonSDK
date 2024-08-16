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
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, constr, validator
from lusid.models.cds_flow_conventions import CdsFlowConventions
from lusid.models.cds_protection_detail_specification import CdsProtectionDetailSpecification
from lusid.models.flow_convention_name import FlowConventionName
from lusid.models.lusid_instrument import LusidInstrument

class CreditDefaultSwap(LusidInstrument):
    """
    LUSID representation of a Credit Default Swap (CDS).                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | ProtectionLeg | Cash flows occurring in the case of default. |  | 2 | PremiumLeg | The premium payments made by the protection buyer. |  # noqa: E501
    """
    ticker: constr(strict=True, min_length=1) = Field(..., description="A ticker to uniquely specify then entity against which the cds is written.")
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.")
    flow_conventions: Optional[CdsFlowConventions] = Field(None, alias="flowConventions")
    coupon_rate: Union[StrictFloat, StrictInt] = Field(..., alias="couponRate", description="The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps.")
    convention_name: Optional[FlowConventionName] = Field(None, alias="conventionName")
    notional: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The notional protected by the Credit Default Swap")
    protection_detail_specification: CdsProtectionDetailSpecification = Field(..., alias="protectionDetailSpecification")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "ticker", "startDate", "maturityDate", "flowConventions", "couponRate", "conventionName", "notional", "protectionDetailSpecification"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan', 'UnsettledCash', 'Cash'):
            raise ValueError("must be one of enum values ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan', 'UnsettledCash', 'Cash')")
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
    def from_json(cls, json_str: str) -> CreditDefaultSwap:
        """Create an instance of CreditDefaultSwap from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of flow_conventions
        if self.flow_conventions:
            _dict['flowConventions'] = self.flow_conventions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of convention_name
        if self.convention_name:
            _dict['conventionName'] = self.convention_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of protection_detail_specification
        if self.protection_detail_specification:
            _dict['protectionDetailSpecification'] = self.protection_detail_specification.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if notional (nullable) is None
        # and __fields_set__ contains the field
        if self.notional is None and "notional" in self.__fields_set__:
            _dict['notional'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreditDefaultSwap:
        """Create an instance of CreditDefaultSwap from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreditDefaultSwap.parse_obj(obj)

        _obj = CreditDefaultSwap.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "ticker": obj.get("ticker"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "flow_conventions": CdsFlowConventions.from_dict(obj.get("flowConventions")) if obj.get("flowConventions") is not None else None,
            "coupon_rate": obj.get("couponRate"),
            "convention_name": FlowConventionName.from_dict(obj.get("conventionName")) if obj.get("conventionName") is not None else None,
            "notional": obj.get("notional"),
            "protection_detail_specification": CdsProtectionDetailSpecification.from_dict(obj.get("protectionDetailSpecification")) if obj.get("protectionDetailSpecification") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
