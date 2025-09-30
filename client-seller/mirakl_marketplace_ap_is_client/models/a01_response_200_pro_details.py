from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A01Response200ProDetails")


@_attrs_define
class A01Response200ProDetails:
    """
    Attributes:
        vat_number (Union[Unset, str]): VAT Number (for taxes)
        corporate_name (Union[Unset, str]): Corporate name
        identification_number (Union[Unset, str]): Identification number of the shop. For France it would be the SIRET
        tax_identification_number (Union[Unset, str]): Tax identification number
    """

    vat_number: Union[Unset, str] = UNSET
    corporate_name: Union[Unset, str] = UNSET
    identification_number: Union[Unset, str] = UNSET
    tax_identification_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vat_number = self.vat_number

        corporate_name = self.corporate_name

        identification_number = self.identification_number

        tax_identification_number = self.tax_identification_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vat_number is not UNSET:
            field_dict["VAT_number"] = vat_number
        if corporate_name is not UNSET:
            field_dict["corporate_name"] = corporate_name
        if identification_number is not UNSET:
            field_dict["identification_number"] = identification_number
        if tax_identification_number is not UNSET:
            field_dict["tax_identification_number"] = tax_identification_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vat_number = d.pop("VAT_number", UNSET)

        corporate_name = d.pop("corporate_name", UNSET)

        identification_number = d.pop("identification_number", UNSET)

        tax_identification_number = d.pop("tax_identification_number", UNSET)

        a01_response_200_pro_details = cls(
            vat_number=vat_number,
            corporate_name=corporate_name,
            identification_number=identification_number,
            tax_identification_number=tax_identification_number,
        )

        a01_response_200_pro_details.additional_properties = d
        return a01_response_200_pro_details

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
