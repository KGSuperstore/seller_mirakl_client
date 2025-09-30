import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DR11Response200DataInitialDocuments")


@_attrs_define
class DR11Response200DataInitialDocuments:
    """
    Attributes:
        id (Union[Unset, str]): The initial document request unique identifier
        issue_date (Union[Unset, datetime.datetime]): The initial document request issue date
        number (Union[Unset, str]): The initial document accounting number
        type_ (Union[Unset, str]): The initial document request type
    """

    id: Union[Unset, str] = UNSET
    issue_date: Union[Unset, datetime.datetime] = UNSET
    number: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        number = self.number

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if number is not UNSET:
            field_dict["number"] = number
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: Union[Unset, datetime.datetime]
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date)

        number = d.pop("number", UNSET)

        type_ = d.pop("type", UNSET)

        dr11_response_200_data_initial_documents = cls(
            id=id,
            issue_date=issue_date,
            number=number,
            type_=type_,
        )

        dr11_response_200_data_initial_documents.additional_properties = d
        return dr11_response_200_data_initial_documents

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
