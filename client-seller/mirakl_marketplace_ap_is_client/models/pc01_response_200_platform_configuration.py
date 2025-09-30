from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pc01_response_200_platform_configuration_customer_model import (
        PC01Response200PlatformConfigurationCustomerModel,
    )
    from ..models.pc01_response_200_platform_configuration_platform_model import (
        PC01Response200PlatformConfigurationPlatformModel,
    )


T = TypeVar("T", bound="PC01Response200PlatformConfiguration")


@_attrs_define
class PC01Response200PlatformConfiguration:
    """
    Attributes:
        customer_model (Union[Unset, PC01Response200PlatformConfigurationCustomerModel]):
        platform_model (Union[Unset, PC01Response200PlatformConfigurationPlatformModel]):
    """

    customer_model: Union[Unset, "PC01Response200PlatformConfigurationCustomerModel"] = UNSET
    platform_model: Union[Unset, "PC01Response200PlatformConfigurationPlatformModel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer_model, Unset):
            customer_model = self.customer_model.to_dict()

        platform_model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.platform_model, Unset):
            platform_model = self.platform_model.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_model is not UNSET:
            field_dict["customer_model"] = customer_model
        if platform_model is not UNSET:
            field_dict["platform_model"] = platform_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pc01_response_200_platform_configuration_customer_model import (
            PC01Response200PlatformConfigurationCustomerModel,
        )
        from ..models.pc01_response_200_platform_configuration_platform_model import (
            PC01Response200PlatformConfigurationPlatformModel,
        )

        d = dict(src_dict)
        _customer_model = d.pop("customer_model", UNSET)
        customer_model: Union[Unset, PC01Response200PlatformConfigurationCustomerModel]
        if isinstance(_customer_model, Unset):
            customer_model = UNSET
        else:
            customer_model = PC01Response200PlatformConfigurationCustomerModel.from_dict(_customer_model)

        _platform_model = d.pop("platform_model", UNSET)
        platform_model: Union[Unset, PC01Response200PlatformConfigurationPlatformModel]
        if isinstance(_platform_model, Unset):
            platform_model = UNSET
        else:
            platform_model = PC01Response200PlatformConfigurationPlatformModel.from_dict(_platform_model)

        pc01_response_200_platform_configuration = cls(
            customer_model=customer_model,
            platform_model=platform_model,
        )

        pc01_response_200_platform_configuration.additional_properties = d
        return pc01_response_200_platform_configuration

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
