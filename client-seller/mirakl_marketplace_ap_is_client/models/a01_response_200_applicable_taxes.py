from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A01Response200ApplicableTaxes")


@_attrs_define
class A01Response200ApplicableTaxes:
    """
    Attributes:
        code (Union[Unset, str]): Tax code
        fee_types (Union[Unset, list[str]]): The types of fees to which the tax will be applied.
        label (Union[Unset, str]): Tax label
    """

    code: Union[Unset, str] = UNSET
    fee_types: Union[Unset, list[str]] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        fee_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fee_types, Unset):
            fee_types = self.fee_types

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if fee_types is not UNSET:
            field_dict["fee_types"] = fee_types
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        fee_types = cast(list[str], d.pop("fee_types", UNSET))

        label = d.pop("label", UNSET)

        a01_response_200_applicable_taxes = cls(
            code=code,
            fee_types=fee_types,
            label=label,
        )

        a01_response_200_applicable_taxes.additional_properties = d
        return a01_response_200_applicable_taxes

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
