from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SH31Response200LogisticClasses")


@_attrs_define
class SH31Response200LogisticClasses:
    """
    Attributes:
        code (Union[Unset, str]): Logistic class code
        description (Union[Unset, str]): Logistic class description
        label (Union[Unset, str]): Logistic class label
    """

    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        description = self.description

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        label = d.pop("label", UNSET)

        sh31_response_200_logistic_classes = cls(
            code=code,
            description=description,
            label=label,
        )

        sh31_response_200_logistic_classes.additional_properties = d
        return sh31_response_200_logistic_classes

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
