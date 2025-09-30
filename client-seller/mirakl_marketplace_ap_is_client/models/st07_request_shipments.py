from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st07_request_shipments_shipping_from import ST07RequestShipmentsShippingFrom


T = TypeVar("T", bound="ST07RequestShipments")


@_attrs_define
class ST07RequestShipments:
    """Shipments list

    Attributes:
        id (Union[Unset, str]): The shipment id
        shipping_from (Union[Unset, ST07RequestShipmentsShippingFrom]): Shipment's shipping origin
    """

    id: Union[Unset, str] = UNSET
    shipping_from: Union[Unset, "ST07RequestShipmentsShippingFrom"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        shipping_from: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_from, Unset):
            shipping_from = self.shipping_from.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if shipping_from is not UNSET:
            field_dict["shipping_from"] = shipping_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st07_request_shipments_shipping_from import ST07RequestShipmentsShippingFrom

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _shipping_from = d.pop("shipping_from", UNSET)
        shipping_from: Union[Unset, ST07RequestShipmentsShippingFrom]
        if isinstance(_shipping_from, Unset):
            shipping_from = UNSET
        else:
            shipping_from = ST07RequestShipmentsShippingFrom.from_dict(_shipping_from)

        st07_request_shipments = cls(
            id=id,
            shipping_from=shipping_from,
        )

        st07_request_shipments.additional_properties = d
        return st07_request_shipments

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
