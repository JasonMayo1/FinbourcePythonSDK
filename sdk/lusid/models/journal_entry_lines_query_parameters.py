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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from lusid.models.date_or_diary_entry import DateOrDiaryEntry

class JournalEntryLinesQueryParameters(BaseModel):
    """
    JournalEntryLinesQueryParameters
    """
    start: Optional[DateOrDiaryEntry] = None
    end: Optional[DateOrDiaryEntry] = None
    date_mode: Optional[StrictStr] = Field(None, alias="dateMode", description="The mode of calculation of the journal entry lines. The available values are: ActivityDate, AccountingDate.")
    general_ledger_profile_code: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="generalLedgerProfileCode", description="The optional code of a general ledger profile used to decorate journal entry lines with levels.")
    property_keys: Optional[conlist(StrictStr)] = Field(None, alias="propertyKeys", description="A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', 'Account', 'LegalEntity' or 'CustodianAccount' domain to decorate onto the journal entry lines.")
    __properties = ["start", "end", "dateMode", "generalLedgerProfileCode", "propertyKeys"]

    @validator('general_ledger_profile_code')
    def general_ledger_profile_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
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
    def from_json(cls, json_str: str) -> JournalEntryLinesQueryParameters:
        """Create an instance of JournalEntryLinesQueryParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of start
        if self.start:
            _dict['start'] = self.start.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end
        if self.end:
            _dict['end'] = self.end.to_dict()
        # set to None if date_mode (nullable) is None
        # and __fields_set__ contains the field
        if self.date_mode is None and "date_mode" in self.__fields_set__:
            _dict['dateMode'] = None

        # set to None if general_ledger_profile_code (nullable) is None
        # and __fields_set__ contains the field
        if self.general_ledger_profile_code is None and "general_ledger_profile_code" in self.__fields_set__:
            _dict['generalLedgerProfileCode'] = None

        # set to None if property_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.property_keys is None and "property_keys" in self.__fields_set__:
            _dict['propertyKeys'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JournalEntryLinesQueryParameters:
        """Create an instance of JournalEntryLinesQueryParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JournalEntryLinesQueryParameters.parse_obj(obj)

        _obj = JournalEntryLinesQueryParameters.parse_obj({
            "start": DateOrDiaryEntry.from_dict(obj.get("start")) if obj.get("start") is not None else None,
            "end": DateOrDiaryEntry.from_dict(obj.get("end")) if obj.get("end") is not None else None,
            "date_mode": obj.get("dateMode"),
            "general_ledger_profile_code": obj.get("generalLedgerProfileCode"),
            "property_keys": obj.get("propertyKeys")
        })
        return _obj
