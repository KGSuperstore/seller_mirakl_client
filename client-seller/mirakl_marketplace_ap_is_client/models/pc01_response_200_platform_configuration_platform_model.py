from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200PlatformConfigurationPlatformModel")


@_attrs_define
class PC01Response200PlatformConfigurationPlatformModel:
    """
    Attributes:
        drop_ship (Union[Unset, bool]): Drop ship platform model activated
        marketplace (Union[Unset, bool]): Marketplace platform model activated
        one_creditor (Union[Unset, bool]): One creditor platform model activated
    """

    drop_ship: Union[Unset, bool] = UNSET
    marketplace: Union[Unset, bool] = UNSET
    one_creditor: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        drop_ship = self.drop_ship

        marketplace = self.marketplace

        one_creditor = self.one_creditor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if drop_ship is not UNSET:
            field_dict["drop_ship"] = drop_ship
        if marketplace is not UNSET:
            field_dict["marketplace"] = marketplace
        if one_creditor is not UNSET:
            field_dict["one_creditor"] = one_creditor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        drop_ship = d.pop("drop_ship", UNSET)

        marketplace = d.pop("marketplace", UNSET)

        one_creditor = d.pop("one_creditor", UNSET)

        pc01_response_200_platform_configuration_platform_model = cls(
            drop_ship=drop_ship,
            marketplace=marketplace,
            one_creditor=one_creditor,
        )

        pc01_response_200_platform_configuration_platform_model.additional_properties = d
        return pc01_response_200_platform_configuration_platform_model

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
