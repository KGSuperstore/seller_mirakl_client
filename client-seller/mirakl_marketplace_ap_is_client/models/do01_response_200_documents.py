from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DO01Response200Documents")


@_attrs_define
class DO01Response200Documents:
    """
    Attributes:
        code (Union[Unset, str]): Type code
        description (Union[Unset, str]): Type description
        entity (Union[Unset, str]): Entity type linked to the document type
        label (Union[Unset, str]): Type label
        mime_types (Union[Unset, list[str]]): Authorized mime types
    """

    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    entity: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    mime_types: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        description = self.description

        entity = self.entity

        label = self.label

        mime_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mime_types, Unset):
            mime_types = self.mime_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if entity is not UNSET:
            field_dict["entity"] = entity
        if label is not UNSET:
            field_dict["label"] = label
        if mime_types is not UNSET:
            field_dict["mime_types"] = mime_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        entity = d.pop("entity", UNSET)

        label = d.pop("label", UNSET)

        mime_types = cast(list[str], d.pop("mime_types", UNSET))

        do01_response_200_documents = cls(
            code=code,
            description=description,
            entity=entity,
            label=label,
            mime_types=mime_types,
        )

        do01_response_200_documents.additional_properties = d
        return do01_response_200_documents

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
