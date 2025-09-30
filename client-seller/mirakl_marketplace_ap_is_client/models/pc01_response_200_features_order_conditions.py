from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200FeaturesOrderConditions")


@_attrs_define
class PC01Response200FeaturesOrderConditions:
    """
    Attributes:
        lead_time_to_ship (Union[Unset, bool]): Allows sellers to inform a lead time to ship on their offers
        maximum_order_quantity (Union[Unset, bool]): Allows sellers to request for a maximum order quantity
        minimum_order_quantity (Union[Unset, bool]): Allows sellers to request for a minimum order quantity
        package_order_quantity (Union[Unset, bool]): Allows sellers to set an order quantity increment
    """

    lead_time_to_ship: Union[Unset, bool] = UNSET
    maximum_order_quantity: Union[Unset, bool] = UNSET
    minimum_order_quantity: Union[Unset, bool] = UNSET
    package_order_quantity: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lead_time_to_ship = self.lead_time_to_ship

        maximum_order_quantity = self.maximum_order_quantity

        minimum_order_quantity = self.minimum_order_quantity

        package_order_quantity = self.package_order_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lead_time_to_ship is not UNSET:
            field_dict["lead_time_to_ship"] = lead_time_to_ship
        if maximum_order_quantity is not UNSET:
            field_dict["maximum_order_quantity"] = maximum_order_quantity
        if minimum_order_quantity is not UNSET:
            field_dict["minimum_order_quantity"] = minimum_order_quantity
        if package_order_quantity is not UNSET:
            field_dict["package_order_quantity"] = package_order_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lead_time_to_ship = d.pop("lead_time_to_ship", UNSET)

        maximum_order_quantity = d.pop("maximum_order_quantity", UNSET)

        minimum_order_quantity = d.pop("minimum_order_quantity", UNSET)

        package_order_quantity = d.pop("package_order_quantity", UNSET)

        pc01_response_200_features_order_conditions = cls(
            lead_time_to_ship=lead_time_to_ship,
            maximum_order_quantity=maximum_order_quantity,
            minimum_order_quantity=minimum_order_quantity,
            package_order_quantity=package_order_quantity,
        )

        pc01_response_200_features_order_conditions.additional_properties = d
        return pc01_response_200_features_order_conditions

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
