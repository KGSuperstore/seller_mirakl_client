import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR14Response200")


@_attrs_define
class OR14Response200:
    """
    Attributes:
        last_updated (Union[Unset, datetime.datetime]): The last updated date of the export
        status (Union[Unset, str]): Current status of the export, can be 'PENDING', 'FAILED', or 'COMPLETED'
        urls (Union[Unset, list[str]]): List of generated URLs to call to download each generated chunks
    """

    last_updated: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    urls: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        status = self.status

        urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if status is not UNSET:
            field_dict["status"] = status
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _last_updated = d.pop("last_updated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        status = d.pop("status", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))

        or14_response_200 = cls(
            last_updated=last_updated,
            status=status,
            urls=urls,
        )

        or14_response_200.additional_properties = d
        return or14_response_200

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
