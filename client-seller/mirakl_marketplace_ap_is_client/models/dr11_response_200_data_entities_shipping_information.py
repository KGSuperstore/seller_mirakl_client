from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr11_response_200_data_entities_shipping_information_ship_to_address import (
        DR11Response200DataEntitiesShippingInformationShipToAddress,
    )


T = TypeVar("T", bound="DR11Response200DataEntitiesShippingInformation")


@_attrs_define
class DR11Response200DataEntitiesShippingInformation:
    """
    Attributes:
        ship_to_address (Union[Unset, DR11Response200DataEntitiesShippingInformationShipToAddress]):
    """

    ship_to_address: Union[Unset, "DR11Response200DataEntitiesShippingInformationShipToAddress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ship_to_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_address, Unset):
            ship_to_address = self.ship_to_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ship_to_address is not UNSET:
            field_dict["ship_to_address"] = ship_to_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr11_response_200_data_entities_shipping_information_ship_to_address import (
            DR11Response200DataEntitiesShippingInformationShipToAddress,
        )

        d = dict(src_dict)
        _ship_to_address = d.pop("ship_to_address", UNSET)
        ship_to_address: Union[Unset, DR11Response200DataEntitiesShippingInformationShipToAddress]
        if isinstance(_ship_to_address, Unset):
            ship_to_address = UNSET
        else:
            ship_to_address = DR11Response200DataEntitiesShippingInformationShipToAddress.from_dict(_ship_to_address)

        dr11_response_200_data_entities_shipping_information = cls(
            ship_to_address=ship_to_address,
        )

        dr11_response_200_data_entities_shipping_information.additional_properties = d
        return dr11_response_200_data_entities_shipping_information

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
