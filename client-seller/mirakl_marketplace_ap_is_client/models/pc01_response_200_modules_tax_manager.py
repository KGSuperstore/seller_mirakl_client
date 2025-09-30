from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pc01_response_200_modules_tax_manager_tax_provider import PC01Response200ModulesTaxManagerTaxProvider


T = TypeVar("T", bound="PC01Response200ModulesTaxManager")


@_attrs_define
class PC01Response200ModulesTaxManager:
    """
    Attributes:
        activated (Union[Unset, bool]): Tax Manager activated
        tax_provider (Union[Unset, PC01Response200ModulesTaxManagerTaxProvider]):
    """

    activated: Union[Unset, bool] = UNSET
    tax_provider: Union[Unset, "PC01Response200ModulesTaxManagerTaxProvider"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activated = self.activated

        tax_provider: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_provider, Unset):
            tax_provider = self.tax_provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activated is not UNSET:
            field_dict["activated"] = activated
        if tax_provider is not UNSET:
            field_dict["tax_provider"] = tax_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pc01_response_200_modules_tax_manager_tax_provider import (
            PC01Response200ModulesTaxManagerTaxProvider,
        )

        d = dict(src_dict)
        activated = d.pop("activated", UNSET)

        _tax_provider = d.pop("tax_provider", UNSET)
        tax_provider: Union[Unset, PC01Response200ModulesTaxManagerTaxProvider]
        if isinstance(_tax_provider, Unset):
            tax_provider = UNSET
        else:
            tax_provider = PC01Response200ModulesTaxManagerTaxProvider.from_dict(_tax_provider)

        pc01_response_200_modules_tax_manager = cls(
            activated=activated,
            tax_provider=tax_provider,
        )

        pc01_response_200_modules_tax_manager.additional_properties = d
        return pc01_response_200_modules_tax_manager

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
