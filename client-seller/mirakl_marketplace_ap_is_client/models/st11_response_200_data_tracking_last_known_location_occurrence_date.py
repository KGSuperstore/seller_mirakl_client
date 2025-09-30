import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ST11Response200DataTrackingLastKnownLocationOccurrenceDate")


@_attrs_define
class ST11Response200DataTrackingLastKnownLocationOccurrenceDate:
    """
    Attributes:
        date (Union[Unset, datetime.date]): Date
        offset (Union[Unset, str]): Zone offset, with the following format (compliant with ISO8601) : ±hh:mm. The offset
            +00:00 can be replaced by Z (the zero UTC offset).
        time (Union[Unset, str]): Time, with the following format (compliant with ISO8601) : hh:mm[:ss]
    """

    date: Union[Unset, datetime.date] = UNSET
    offset: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        offset = self.offset

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if offset is not UNSET:
            field_dict["offset"] = offset
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        offset = d.pop("offset", UNSET)

        time = d.pop("time", UNSET)

        st11_response_200_data_tracking_last_known_location_occurrence_date = cls(
            date=date,
            offset=offset,
            time=time,
        )

        st11_response_200_data_tracking_last_known_location_occurrence_date.additional_properties = d
        return st11_response_200_data_tracking_last_known_location_occurrence_date

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
