from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ST01RequestShipmentsShipmentLines")


@_attrs_define
class ST01RequestShipmentsShipmentLines:
    """Shipment lines

    Attributes:
        offer_sku (Union[Unset, str]): Offer sku
        order_line_id (Union[Unset, str]): Order line id
        package_reference (Union[Unset, str]): Package reference
        quantity (Union[Unset, int]): Quantity
    """

    offer_sku: Union[Unset, str] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    package_reference: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offer_sku = self.offer_sku

        order_line_id = self.order_line_id

        package_reference = self.package_reference

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offer_sku is not UNSET:
            field_dict["offer_sku"] = offer_sku
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if package_reference is not UNSET:
            field_dict["package_reference"] = package_reference
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offer_sku = d.pop("offer_sku", UNSET)

        order_line_id = d.pop("order_line_id", UNSET)

        package_reference = d.pop("package_reference", UNSET)

        quantity = d.pop("quantity", UNSET)

        st01_request_shipments_shipment_lines = cls(
            offer_sku=offer_sku,
            order_line_id=order_line_id,
            package_reference=package_reference,
            quantity=quantity,
        )

        st01_request_shipments_shipment_lines.additional_properties = d
        return st01_request_shipments_shipment_lines

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
