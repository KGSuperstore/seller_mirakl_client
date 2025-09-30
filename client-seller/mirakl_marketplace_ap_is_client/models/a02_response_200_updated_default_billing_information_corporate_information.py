from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a02_response_200_updated_default_billing_information_corporate_information_complementary_information import (
        A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation,
    )


T = TypeVar("T", bound="A02Response200UpdatedDefaultBillingInformationCorporateInformation")


@_attrs_define
class A02Response200UpdatedDefaultBillingInformationCorporateInformation:
    """
    Attributes:
        company_registration_name (Union[Unset, str]): The name of the shop company, as registered in the business
            registry of the shop country
        company_registration_number (Union[Unset, str]): The unique code used to identify the shop company and verify
            its legal existence as an incorporated entity
        complementary_information (Union[Unset,
            A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation]):
    """

    company_registration_name: Union[Unset, str] = UNSET
    company_registration_number: Union[Unset, str] = UNSET
    complementary_information: Union[
        Unset, "A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_registration_name = self.company_registration_name

        company_registration_number = self.company_registration_number

        complementary_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.complementary_information, Unset):
            complementary_information = self.complementary_information.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_registration_name is not UNSET:
            field_dict["company_registration_name"] = company_registration_name
        if company_registration_number is not UNSET:
            field_dict["company_registration_number"] = company_registration_number
        if complementary_information is not UNSET:
            field_dict["complementary_information"] = complementary_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.a02_response_200_updated_default_billing_information_corporate_information_complementary_information import (
            A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation,
        )

        d = dict(src_dict)
        company_registration_name = d.pop("company_registration_name", UNSET)

        company_registration_number = d.pop("company_registration_number", UNSET)

        _complementary_information = d.pop("complementary_information", UNSET)
        complementary_information: Union[
            Unset, A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation
        ]
        if isinstance(_complementary_information, Unset):
            complementary_information = UNSET
        else:
            complementary_information = (
                A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation.from_dict(
                    _complementary_information
                )
            )

        a02_response_200_updated_default_billing_information_corporate_information = cls(
            company_registration_name=company_registration_name,
            company_registration_number=company_registration_number,
            complementary_information=complementary_information,
        )

        a02_response_200_updated_default_billing_information_corporate_information.additional_properties = d
        return a02_response_200_updated_default_billing_information_corporate_information

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
