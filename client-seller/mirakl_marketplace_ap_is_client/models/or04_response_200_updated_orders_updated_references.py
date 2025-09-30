from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR04Response200UpdatedOrdersUpdatedReferences")


@_attrs_define
class OR04Response200UpdatedOrdersUpdatedReferences:
    """
    Attributes:
        order_reference_for_seller (Union[Unset, str]): Order reference for seller
    """

    order_reference_for_seller: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_reference_for_seller = self.order_reference_for_seller

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_reference_for_seller is not UNSET:
            field_dict["order_reference_for_seller"] = order_reference_for_seller

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_reference_for_seller = d.pop("order_reference_for_seller", UNSET)

        or04_response_200_updated_orders_updated_references = cls(
            order_reference_for_seller=order_reference_for_seller,
        )

        or04_response_200_updated_orders_updated_references.additional_properties = d
        return or04_response_200_updated_orders_updated_references

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
