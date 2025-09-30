from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="P11Response200ProductsProductReferences")


@_attrs_define
class P11Response200ProductsProductReferences:
    """
    Attributes:
        reference (Union[Unset, str]): Value of the reference
        reference_type (Union[Unset, str]): Type of the reference
    """

    reference: Union[Unset, str] = UNSET
    reference_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        reference_type = self.reference_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_type is not UNSET:
            field_dict["reference_type"] = reference_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference = d.pop("reference", UNSET)

        reference_type = d.pop("reference_type", UNSET)

        p11_response_200_products_product_references = cls(
            reference=reference,
            reference_type=reference_type,
        )

        p11_response_200_products_product_references.additional_properties = d
        return p11_response_200_products_product_references

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
