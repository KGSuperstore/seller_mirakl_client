from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ST12Response200DataShipmentLines")


@_attrs_define
class ST12Response200DataShipmentLines:
    """
    Attributes:
        offer_sku (Union[Unset, str]): Offer sku
        order_line_id (Union[Unset, str]): Order line id
        package_description (Union[Unset, str]): Package Description
        package_reference (Union[Unset, str]): Package reference
        product_title (Union[Unset, str]): Product title
        quantity (Union[Unset, int]): Quantity
    """

    offer_sku: Union[Unset, str] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    package_description: Union[Unset, str] = UNSET
    package_reference: Union[Unset, str] = UNSET
    product_title: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offer_sku = self.offer_sku

        order_line_id = self.order_line_id

        package_description = self.package_description

        package_reference = self.package_reference

        product_title = self.product_title

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offer_sku is not UNSET:
            field_dict["offer_sku"] = offer_sku
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if package_description is not UNSET:
            field_dict["package_description"] = package_description
        if package_reference is not UNSET:
            field_dict["package_reference"] = package_reference
        if product_title is not UNSET:
            field_dict["product_title"] = product_title
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offer_sku = d.pop("offer_sku", UNSET)

        order_line_id = d.pop("order_line_id", UNSET)

        package_description = d.pop("package_description", UNSET)

        package_reference = d.pop("package_reference", UNSET)

        product_title = d.pop("product_title", UNSET)

        quantity = d.pop("quantity", UNSET)

        st12_response_200_data_shipment_lines = cls(
            offer_sku=offer_sku,
            order_line_id=order_line_id,
            package_description=package_description,
            package_reference=package_reference,
            product_title=product_title,
            quantity=quantity,
        )

        st12_response_200_data_shipment_lines.additional_properties = d
        return st12_response_200_data_shipment_lines

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
