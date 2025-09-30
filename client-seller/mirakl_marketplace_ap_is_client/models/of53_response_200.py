import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of53_response_200_error import OF53Response200Error


T = TypeVar("T", bound="OF53Response200")


@_attrs_define
class OF53Response200:
    """
    Attributes:
        error (Union[Unset, OF53Response200Error]):
        last_updated (Union[Unset, datetime.datetime]): The last update date of the export
        status (Union[Unset, str]): Current status of the export, can be <code>PENDING</code>, <code>FAILED</code> or
            <code>COMPLETED</code>
        urls (Union[Unset, list[str]]): List of generated urls to call to download each generated chunks
    """

    error: Union[Unset, "OF53Response200Error"] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    urls: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

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
        if error is not UNSET:
            field_dict["error"] = error
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if status is not UNSET:
            field_dict["status"] = status
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of53_response_200_error import OF53Response200Error

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, OF53Response200Error]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = OF53Response200Error.from_dict(_error)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        status = d.pop("status", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))

        of53_response_200 = cls(
            error=error,
            last_updated=last_updated,
            status=status,
            urls=urls,
        )

        of53_response_200.additional_properties = d
        return of53_response_200

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
