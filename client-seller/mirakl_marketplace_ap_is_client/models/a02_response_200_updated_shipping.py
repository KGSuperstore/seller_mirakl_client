from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A02Response200UpdatedShipping")


@_attrs_define
class A02Response200UpdatedShipping:
    """
    Attributes:
        lead_time_to_ship (Union[Unset, int]): Default lead time to ship of the shop
    """

    lead_time_to_ship: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lead_time_to_ship = self.lead_time_to_ship

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lead_time_to_ship is not UNSET:
            field_dict["lead_time_to_ship"] = lead_time_to_ship

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lead_time_to_ship = d.pop("lead_time_to_ship", UNSET)

        a02_response_200_updated_shipping = cls(
            lead_time_to_ship=lead_time_to_ship,
        )

        a02_response_200_updated_shipping.additional_properties = d
        return a02_response_200_updated_shipping

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
