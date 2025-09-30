from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200FeaturesShipment")


@_attrs_define
class PC01Response200FeaturesShipment:
    """
    Attributes:
        multi_part_item_shipment (Union[Unset, bool]): Allows sellers to create several packages for a same item in an
            order
        multi_shipment (Union[Unset, bool]): Allows sellers to create several shipments for a same order
    """

    multi_part_item_shipment: Union[Unset, bool] = UNSET
    multi_shipment: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        multi_part_item_shipment = self.multi_part_item_shipment

        multi_shipment = self.multi_shipment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if multi_part_item_shipment is not UNSET:
            field_dict["multi_part_item_shipment"] = multi_part_item_shipment
        if multi_shipment is not UNSET:
            field_dict["multi_shipment"] = multi_shipment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        multi_part_item_shipment = d.pop("multi_part_item_shipment", UNSET)

        multi_shipment = d.pop("multi_shipment", UNSET)

        pc01_response_200_features_shipment = cls(
            multi_part_item_shipment=multi_part_item_shipment,
            multi_shipment=multi_shipment,
        )

        pc01_response_200_features_shipment.additional_properties = d
        return pc01_response_200_features_shipment

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
