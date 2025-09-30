import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="S30Response200ShopDocuments")


@_attrs_define
class S30Response200ShopDocuments:
    """
    Attributes:
        date_uploaded (Union[Unset, datetime.datetime]): Document uploaded date
        file_name (Union[Unset, str]): Document file name
        id (Union[Unset, int]): Document identifier
        type_ (Union[Unset, str]): Document type code
    """

    date_uploaded: Union[Unset, datetime.datetime] = UNSET
    file_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_uploaded: Union[Unset, str] = UNSET
        if not isinstance(self.date_uploaded, Unset):
            date_uploaded = self.date_uploaded.isoformat()

        file_name = self.file_name

        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_uploaded is not UNSET:
            field_dict["date_uploaded"] = date_uploaded
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_uploaded = d.pop("date_uploaded", UNSET)
        date_uploaded: Union[Unset, datetime.datetime]
        if isinstance(_date_uploaded, Unset):
            date_uploaded = UNSET
        else:
            date_uploaded = isoparse(_date_uploaded)

        file_name = d.pop("file_name", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        s30_response_200_shop_documents = cls(
            date_uploaded=date_uploaded,
            file_name=file_name,
            id=id,
            type_=type_,
        )

        s30_response_200_shop_documents.additional_properties = d
        return s30_response_200_shop_documents

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
