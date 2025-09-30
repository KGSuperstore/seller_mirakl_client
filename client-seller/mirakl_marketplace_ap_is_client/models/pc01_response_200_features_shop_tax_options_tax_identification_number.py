from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber")


@_attrs_define
class PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber:
    """
    Attributes:
        mandatory (Union[Unset, bool]): Defines if the tax identification number is mandatory
        validation_regex (Union[Unset, str]): Regular expression that the tax identification number must match
    """

    mandatory: Union[Unset, bool] = UNSET
    validation_regex: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mandatory = self.mandatory

        validation_regex = self.validation_regex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if validation_regex is not UNSET:
            field_dict["validation_regex"] = validation_regex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mandatory = d.pop("mandatory", UNSET)

        validation_regex = d.pop("validation_regex", UNSET)

        pc01_response_200_features_shop_tax_options_tax_identification_number = cls(
            mandatory=mandatory,
            validation_regex=validation_regex,
        )

        pc01_response_200_features_shop_tax_options_tax_identification_number.additional_properties = d
        return pc01_response_200_features_shop_tax_options_tax_identification_number

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
