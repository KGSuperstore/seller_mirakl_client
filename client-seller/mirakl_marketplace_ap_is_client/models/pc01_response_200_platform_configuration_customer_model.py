from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200PlatformConfigurationCustomerModel")


@_attrs_define
class PC01Response200PlatformConfigurationCustomerModel:
    """
    Attributes:
        b2b (Union[Unset, bool]): Customer model Business to Business is enabled: if true, customers can be linked to a
            customer organization
        b2c (Union[Unset, bool]): Customer model Business to Customer is enabled: if true, customers can be created
            without being linked to a customer organization
    """

    b2b: Union[Unset, bool] = UNSET
    b2c: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        b2b = self.b2b

        b2c = self.b2c

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if b2b is not UNSET:
            field_dict["b2b"] = b2b
        if b2c is not UNSET:
            field_dict["b2c"] = b2c

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        b2b = d.pop("b2b", UNSET)

        b2c = d.pop("b2c", UNSET)

        pc01_response_200_platform_configuration_customer_model = cls(
            b2b=b2b,
            b2c=b2c,
        )

        pc01_response_200_platform_configuration_customer_model.additional_properties = d
        return pc01_response_200_platform_configuration_customer_model

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
