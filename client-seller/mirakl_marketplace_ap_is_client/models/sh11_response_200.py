from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sh11_response_200_shipping_zones import SH11Response200ShippingZones


T = TypeVar("T", bound="SH11Response200")


@_attrs_define
class SH11Response200:
    """
    Attributes:
        shipping_zones (Union[Unset, list['SH11Response200ShippingZones']]): List of shipping zones
    """

    shipping_zones: Union[Unset, list["SH11Response200ShippingZones"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipping_zones: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_zones, Unset):
            shipping_zones = []
            for shipping_zones_item_data in self.shipping_zones:
                shipping_zones_item = shipping_zones_item_data.to_dict()
                shipping_zones.append(shipping_zones_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipping_zones is not UNSET:
            field_dict["shipping_zones"] = shipping_zones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sh11_response_200_shipping_zones import SH11Response200ShippingZones

        d = dict(src_dict)
        shipping_zones = []
        _shipping_zones = d.pop("shipping_zones", UNSET)
        for shipping_zones_item_data in _shipping_zones or []:
            shipping_zones_item = SH11Response200ShippingZones.from_dict(shipping_zones_item_data)

            shipping_zones.append(shipping_zones_item)

        sh11_response_200 = cls(
            shipping_zones=shipping_zones,
        )

        sh11_response_200.additional_properties = d
        return sh11_response_200

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
