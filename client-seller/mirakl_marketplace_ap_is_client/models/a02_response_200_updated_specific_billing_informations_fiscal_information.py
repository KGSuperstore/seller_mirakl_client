from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A02Response200UpdatedSpecificBillingInformationsFiscalInformation")


@_attrs_define
class A02Response200UpdatedSpecificBillingInformationsFiscalInformation:
    """
    Attributes:
        local_tax_number (Union[Unset, str]): The VAT or GST number of the shop
        tax_identification_country (Union[Unset, str]): The country of issuance of the tax identification number
        tax_identification_number (Union[Unset, str]): The identifying number issued by the tax administration of the
            shop country
    """

    local_tax_number: Union[Unset, str] = UNSET
    tax_identification_country: Union[Unset, str] = UNSET
    tax_identification_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_tax_number = self.local_tax_number

        tax_identification_country = self.tax_identification_country

        tax_identification_number = self.tax_identification_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_tax_number is not UNSET:
            field_dict["local_tax_number"] = local_tax_number
        if tax_identification_country is not UNSET:
            field_dict["tax_identification_country"] = tax_identification_country
        if tax_identification_number is not UNSET:
            field_dict["tax_identification_number"] = tax_identification_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        local_tax_number = d.pop("local_tax_number", UNSET)

        tax_identification_country = d.pop("tax_identification_country", UNSET)

        tax_identification_number = d.pop("tax_identification_number", UNSET)

        a02_response_200_updated_specific_billing_informations_fiscal_information = cls(
            local_tax_number=local_tax_number,
            tax_identification_country=tax_identification_country,
            tax_identification_number=tax_identification_number,
        )

        a02_response_200_updated_specific_billing_informations_fiscal_information.additional_properties = d
        return a02_response_200_updated_specific_billing_informations_fiscal_information

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
