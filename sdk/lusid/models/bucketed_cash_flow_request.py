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
from lusid.models.bucketing_schedule import BucketingSchedule
from lusid.models.resource_id import ResourceId

class BucketedCashFlowRequest(BaseModel):
    """
    Specification class consisting of parameters for BucketedCashFlow endpoint.  # noqa: E501
    """
    rounding_method: constr(strict=True, min_length=1) = Field(..., alias="roundingMethod", description="When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp].")
    bucketing_dates: Optional[conlist(datetime)] = Field(None, alias="bucketingDates", description="A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty.")
    bucket_tenors: Optional[conlist(StrictStr)] = Field(None, alias="bucketTenors", description="A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty.")
    effective_at: Optional[StrictStr] = Field(None, alias="effectiveAt", description="The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today.")
    window_start: Optional[StrictStr] = Field(None, alias="windowStart", description="The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified.")
    window_end: Optional[StrictStr] = Field(None, alias="windowEnd", description="The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to 'today' if it is not specified")
    recipe_id: Optional[ResourceId] = Field(None, alias="recipeId")
    report_currency: Optional[constr(strict=True, max_length=3, min_length=0)] = Field(None, alias="reportCurrency", description="Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.")
    group_by: Optional[conlist(StrictStr)] = Field(None, alias="groupBy", description="The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.")
    addresses: Optional[conlist(StrictStr)] = Field(None, description="The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones.")
    equip_with_subtotals: Optional[StrictBool] = Field(None, alias="equipWithSubtotals", description="Flag directing the Valuation call to populate the results with subtotals of aggregates.")
    as_at: Optional[datetime] = Field(None, alias="asAt", description="The time of the system at which to query for bucketed cashflows.")
    exclude_unsettled_trades: Optional[StrictBool] = Field(None, alias="excludeUnsettledTrades", description="Flag directing the Valuation call to exclude cashflows from unsettled trades.  If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set.")
    cash_flow_type: Optional[StrictStr] = Field(None, alias="cashFlowType", description="Indicate the requested cash flow representation InstrumentCashFlows or PortfolioCashFlows (GetCashLadder uses this)  Options: [InstrumentCashFlow, PortfolioCashFlow]")
    bucketing_schedule: Optional[BucketingSchedule] = Field(None, alias="bucketingSchedule")
    filter: Optional[constr(strict=True, max_length=16384, min_length=0)] = None
    __properties = ["roundingMethod", "bucketingDates", "bucketTenors", "effectiveAt", "windowStart", "windowEnd", "recipeId", "reportCurrency", "groupBy", "addresses", "equipWithSubtotals", "asAt", "excludeUnsettledTrades", "cashFlowType", "bucketingSchedule", "filter"]

    @validator('filter')
    def filter_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> BucketedCashFlowRequest:
        """Create an instance of BucketedCashFlowRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of recipe_id
        if self.recipe_id:
            _dict['recipeId'] = self.recipe_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bucketing_schedule
        if self.bucketing_schedule:
            _dict['bucketingSchedule'] = self.bucketing_schedule.to_dict()
        # set to None if bucketing_dates (nullable) is None
        # and __fields_set__ contains the field
        if self.bucketing_dates is None and "bucketing_dates" in self.__fields_set__:
            _dict['bucketingDates'] = None

        # set to None if bucket_tenors (nullable) is None
        # and __fields_set__ contains the field
        if self.bucket_tenors is None and "bucket_tenors" in self.__fields_set__:
            _dict['bucketTenors'] = None

        # set to None if effective_at (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_at is None and "effective_at" in self.__fields_set__:
            _dict['effectiveAt'] = None

        # set to None if window_start (nullable) is None
        # and __fields_set__ contains the field
        if self.window_start is None and "window_start" in self.__fields_set__:
            _dict['windowStart'] = None

        # set to None if window_end (nullable) is None
        # and __fields_set__ contains the field
        if self.window_end is None and "window_end" in self.__fields_set__:
            _dict['windowEnd'] = None

        # set to None if report_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.report_currency is None and "report_currency" in self.__fields_set__:
            _dict['reportCurrency'] = None

        # set to None if group_by (nullable) is None
        # and __fields_set__ contains the field
        if self.group_by is None and "group_by" in self.__fields_set__:
            _dict['groupBy'] = None

        # set to None if addresses (nullable) is None
        # and __fields_set__ contains the field
        if self.addresses is None and "addresses" in self.__fields_set__:
            _dict['addresses'] = None

        # set to None if as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at is None and "as_at" in self.__fields_set__:
            _dict['asAt'] = None

        # set to None if cash_flow_type (nullable) is None
        # and __fields_set__ contains the field
        if self.cash_flow_type is None and "cash_flow_type" in self.__fields_set__:
            _dict['cashFlowType'] = None

        # set to None if filter (nullable) is None
        # and __fields_set__ contains the field
        if self.filter is None and "filter" in self.__fields_set__:
            _dict['filter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BucketedCashFlowRequest:
        """Create an instance of BucketedCashFlowRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BucketedCashFlowRequest.parse_obj(obj)

        _obj = BucketedCashFlowRequest.parse_obj({
            "rounding_method": obj.get("roundingMethod"),
            "bucketing_dates": obj.get("bucketingDates"),
            "bucket_tenors": obj.get("bucketTenors"),
            "effective_at": obj.get("effectiveAt"),
            "window_start": obj.get("windowStart"),
            "window_end": obj.get("windowEnd"),
            "recipe_id": ResourceId.from_dict(obj.get("recipeId")) if obj.get("recipeId") is not None else None,
            "report_currency": obj.get("reportCurrency"),
            "group_by": obj.get("groupBy"),
            "addresses": obj.get("addresses"),
            "equip_with_subtotals": obj.get("equipWithSubtotals"),
            "as_at": obj.get("asAt"),
            "exclude_unsettled_trades": obj.get("excludeUnsettledTrades"),
            "cash_flow_type": obj.get("cashFlowType"),
            "bucketing_schedule": BucketingSchedule.from_dict(obj.get("bucketingSchedule")) if obj.get("bucketingSchedule") is not None else None,
            "filter": obj.get("filter")
        })
        return _obj
