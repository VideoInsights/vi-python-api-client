# coding: utf-8

"""
    Video Insights

    The Video Insights API endpoint

    The version of the OpenAPI document: 0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from videoinsights_client.models.youtube_statistics import YoutubeStatistics

class YoutubeMetadata(BaseModel):
    """
    YoutubeMetadata
    """
    description: StrictStr = Field(...)
    duration: StrictStr = Field(...)
    license: StrictStr = Field(...)
    made_for_kids: StrictBool = Field(default=..., alias="madeForKids")
    published_at: datetime = Field(default=..., alias="publishedAt")
    statistics: YoutubeStatistics = Field(...)
    tags: conlist(StrictStr) = Field(...)
    title: StrictStr = Field(...)
    __properties = ["description", "duration", "license", "madeForKids", "publishedAt", "statistics", "tags", "title"]

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
    def from_json(cls, json_str: str) -> YoutubeMetadata:
        """Create an instance of YoutubeMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> YoutubeMetadata:
        """Create an instance of YoutubeMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return YoutubeMetadata.parse_obj(obj)

        _obj = YoutubeMetadata.parse_obj({
            "description": obj.get("description"),
            "duration": obj.get("duration"),
            "license": obj.get("license"),
            "made_for_kids": obj.get("madeForKids"),
            "published_at": obj.get("publishedAt"),
            "statistics": YoutubeStatistics.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None,
            "tags": obj.get("tags"),
            "title": obj.get("title")
        })
        return _obj


