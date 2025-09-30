from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pc01_response_200_features_shop_tax_options_local_tax_number import (
        PC01Response200FeaturesShopTaxOptionsLocalTaxNumber,
    )
    from ..models.pc01_response_200_features_shop_tax_options_tax_identification_number import (
        PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber,
    )


T = TypeVar("T", bound="PC01Response200FeaturesShopTaxOptions")


@_attrs_define
class PC01Response200FeaturesShopTaxOptions:
    """
    Attributes:
        local_tax_number (Union[Unset, PC01Response200FeaturesShopTaxOptionsLocalTaxNumber]):
        tax_identification_number (Union[Unset, PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber]):
    """

    local_tax_number: Union[Unset, "PC01Response200FeaturesShopTaxOptionsLocalTaxNumber"] = UNSET
    tax_identification_number: Union[Unset, "PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_tax_number: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.local_tax_number, Unset):
            local_tax_number = self.local_tax_number.to_dict()

        tax_identification_number: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_identification_number, Unset):
            tax_identification_number = self.tax_identification_number.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_tax_number is not UNSET:
            field_dict["local_tax_number"] = local_tax_number
        if tax_identification_number is not UNSET:
            field_dict["tax_identification_number"] = tax_identification_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pc01_response_200_features_shop_tax_options_local_tax_number import (
            PC01Response200FeaturesShopTaxOptionsLocalTaxNumber,
        )
        from ..models.pc01_response_200_features_shop_tax_options_tax_identification_number import (
            PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber,
        )

        d = dict(src_dict)
        _local_tax_number = d.pop("local_tax_number", UNSET)
        local_tax_number: Union[Unset, PC01Response200FeaturesShopTaxOptionsLocalTaxNumber]
        if isinstance(_local_tax_number, Unset):
            local_tax_number = UNSET
        else:
            local_tax_number = PC01Response200FeaturesShopTaxOptionsLocalTaxNumber.from_dict(_local_tax_number)

        _tax_identification_number = d.pop("tax_identification_number", UNSET)
        tax_identification_number: Union[Unset, PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber]
        if isinstance(_tax_identification_number, Unset):
            tax_identification_number = UNSET
        else:
            tax_identification_number = PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber.from_dict(
                _tax_identification_number
            )

        pc01_response_200_features_shop_tax_options = cls(
            local_tax_number=local_tax_number,
            tax_identification_number=tax_identification_number,
        )

        pc01_response_200_features_shop_tax_options.additional_properties = d
        return pc01_response_200_features_shop_tax_options

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
