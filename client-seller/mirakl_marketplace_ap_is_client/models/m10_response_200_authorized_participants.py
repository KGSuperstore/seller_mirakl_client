from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="M10Response200AuthorizedParticipants")


@_attrs_define
class M10Response200AuthorizedParticipants:
    """
    Attributes:
        display_name (Union[Unset, str]): Participant display name
        id (Union[Unset, str]): Participant id<br/>When <code>type</code> equals <code>OPERATOR</code>, no id will be
            returned.
        type_ (Union[Unset, str]): Participant type
    """

    display_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        m10_response_200_authorized_participants = cls(
            display_name=display_name,
            id=id,
            type_=type_,
        )

        m10_response_200_authorized_participants.additional_properties = d
        return m10_response_200_authorized_participants

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
