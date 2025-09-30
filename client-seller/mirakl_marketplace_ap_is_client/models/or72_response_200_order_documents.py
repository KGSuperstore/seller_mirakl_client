import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR72Response200OrderDocuments")


@_attrs_define
class OR72Response200OrderDocuments:
    """
    Attributes:
        date_uploaded (Union[Unset, datetime.datetime]): Document uploaded date
        file_name (Union[Unset, str]): Document file name
        file_size (Union[Unset, int]): Document file size
        id (Union[Unset, int]): Document identifier
        order_id (Union[Unset, str]): The id of the order owning the document
        type_ (Union[Unset, str]): Document type code
    """

    date_uploaded: Union[Unset, datetime.datetime] = UNSET
    file_name: Union[Unset, str] = UNSET
    file_size: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    order_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_uploaded: Union[Unset, str] = UNSET
        if not isinstance(self.date_uploaded, Unset):
            date_uploaded = self.date_uploaded.isoformat()

        file_name = self.file_name

        file_size = self.file_size

        id = self.id

        order_id = self.order_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_uploaded is not UNSET:
            field_dict["date_uploaded"] = date_uploaded
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if id is not UNSET:
            field_dict["id"] = id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
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

        file_size = d.pop("file_size", UNSET)

        id = d.pop("id", UNSET)

        order_id = d.pop("order_id", UNSET)

        type_ = d.pop("type", UNSET)

        or72_response_200_order_documents = cls(
            date_uploaded=date_uploaded,
            file_name=file_name,
            file_size=file_size,
            id=id,
            order_id=order_id,
            type_=type_,
        )

        or72_response_200_order_documents.additional_properties = d
        return or72_response_200_order_documents

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
