from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TL02Response200DataEntitiesOrderReferences")


@_attrs_define
class TL02Response200DataEntitiesOrderReferences:
    """
    Attributes:
        order_reference_for_customer (Union[Unset, str]): Order reference for customer.
        order_reference_for_seller (Union[Unset, str]): Order reference for seller.
    """

    order_reference_for_customer: Union[Unset, str] = UNSET
    order_reference_for_seller: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_reference_for_customer = self.order_reference_for_customer

        order_reference_for_seller = self.order_reference_for_seller

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_reference_for_customer is not UNSET:
            field_dict["order_reference_for_customer"] = order_reference_for_customer
        if order_reference_for_seller is not UNSET:
            field_dict["order_reference_for_seller"] = order_reference_for_seller

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_reference_for_customer = d.pop("order_reference_for_customer", UNSET)

        order_reference_for_seller = d.pop("order_reference_for_seller", UNSET)

        tl02_response_200_data_entities_order_references = cls(
            order_reference_for_customer=order_reference_for_customer,
            order_reference_for_seller=order_reference_for_seller,
        )

        tl02_response_200_data_entities_order_references.additional_properties = d
        return tl02_response_200_data_entities_order_references

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
