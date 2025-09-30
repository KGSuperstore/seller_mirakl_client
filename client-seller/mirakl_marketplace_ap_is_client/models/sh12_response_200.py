from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sh12_response_200_shipping_types import SH12Response200ShippingTypes


T = TypeVar("T", bound="SH12Response200")


@_attrs_define
class SH12Response200:
    """
    Attributes:
        shipping_types (Union[Unset, list['SH12Response200ShippingTypes']]): List of shipping types
    """

    shipping_types: Union[Unset, list["SH12Response200ShippingTypes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipping_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_types, Unset):
            shipping_types = []
            for shipping_types_item_data in self.shipping_types:
                shipping_types_item = shipping_types_item_data.to_dict()
                shipping_types.append(shipping_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipping_types is not UNSET:
            field_dict["shipping_types"] = shipping_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sh12_response_200_shipping_types import SH12Response200ShippingTypes

        d = dict(src_dict)
        shipping_types = []
        _shipping_types = d.pop("shipping_types", UNSET)
        for shipping_types_item_data in _shipping_types or []:
            shipping_types_item = SH12Response200ShippingTypes.from_dict(shipping_types_item_data)

            shipping_types.append(shipping_types_item)

        sh12_response_200 = cls(
            shipping_types=shipping_types,
        )

        sh12_response_200.additional_properties = d
        return sh12_response_200

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
