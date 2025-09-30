import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="M11Response200DataNoStoreReplyNeeded")


@_attrs_define
class M11Response200DataNoStoreReplyNeeded:
    """
    Attributes:
        date (Union[Unset, datetime.datetime]): No store reply needed action date
        user_type (Union[Unset, str]): Entity that operated "no store reply needed" action.
    """

    date: Union[Unset, datetime.datetime] = UNSET
    user_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        user_type = self.user_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if user_type is not UNSET:
            field_dict["user_type"] = user_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        user_type = d.pop("user_type", UNSET)

        m11_response_200_data_no_store_reply_needed = cls(
            date=date,
            user_type=user_type,
        )

        m11_response_200_data_no_store_reply_needed.additional_properties = d
        return m11_response_200_data_no_store_reply_needed

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
