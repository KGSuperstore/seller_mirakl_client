from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A02Response200UpdatedDefaultBillingInformationFiscalRepresentative")


@_attrs_define
class A02Response200UpdatedDefaultBillingInformationFiscalRepresentative:
    """
    Attributes:
        city (Union[Unset, str]): The city where the fiscal representative is located.
        civility (Union[Unset, str]): Civility of the fiscal representative
        company_registration_name (Union[Unset, str]): The name of the fiscal representative, as registered if the
            business registry of the fiscal representative's country
        company_registration_number (Union[Unset, str]): The unique code used to identify the fiscal representative and
            verify its legal existence as an incorporated entity
        country_iso_code (Union[Unset, str]): Country ISO 3166-1 code of the fiscal representative address
        first_name (Union[Unset, str]): First name of the fiscal representative
        last_name (Union[Unset, str]): Last name of the fiscal representative
        local_tax_number (Union[Unset, str]): The identifying number of the fiscal representative for VAT or GST
            purposes
        state (Union[Unset, str]): The state/province/region where the fiscal representative is located.
        street_1 (Union[Unset, str]): The first line of address of the fiscal representative
        street_2 (Union[Unset, str]): The second line of address of the fiscal representative
        zip_code (Union[Unset, str]): The Zip/Postal code corresponding to the fiscal representative location
    """

    city: Union[Unset, str] = UNSET
    civility: Union[Unset, str] = UNSET
    company_registration_name: Union[Unset, str] = UNSET
    company_registration_number: Union[Unset, str] = UNSET
    country_iso_code: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    local_tax_number: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    street_1: Union[Unset, str] = UNSET
    street_2: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        civility = self.civility

        company_registration_name = self.company_registration_name

        company_registration_number = self.company_registration_number

        country_iso_code = self.country_iso_code

        first_name = self.first_name

        last_name = self.last_name

        local_tax_number = self.local_tax_number

        state = self.state

        street_1 = self.street_1

        street_2 = self.street_2

        zip_code = self.zip_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if civility is not UNSET:
            field_dict["civility"] = civility
        if company_registration_name is not UNSET:
            field_dict["company_registration_name"] = company_registration_name
        if company_registration_number is not UNSET:
            field_dict["company_registration_number"] = company_registration_number
        if country_iso_code is not UNSET:
            field_dict["country_iso_code"] = country_iso_code
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if local_tax_number is not UNSET:
            field_dict["local_tax_number"] = local_tax_number
        if state is not UNSET:
            field_dict["state"] = state
        if street_1 is not UNSET:
            field_dict["street_1"] = street_1
        if street_2 is not UNSET:
            field_dict["street_2"] = street_2
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        civility = d.pop("civility", UNSET)

        company_registration_name = d.pop("company_registration_name", UNSET)

        company_registration_number = d.pop("company_registration_number", UNSET)

        country_iso_code = d.pop("country_iso_code", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        local_tax_number = d.pop("local_tax_number", UNSET)

        state = d.pop("state", UNSET)

        street_1 = d.pop("street_1", UNSET)

        street_2 = d.pop("street_2", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        a02_response_200_updated_default_billing_information_fiscal_representative = cls(
            city=city,
            civility=civility,
            company_registration_name=company_registration_name,
            company_registration_number=company_registration_number,
            country_iso_code=country_iso_code,
            first_name=first_name,
            last_name=last_name,
            local_tax_number=local_tax_number,
            state=state,
            street_1=street_1,
            street_2=street_2,
            zip_code=zip_code,
        )

        a02_response_200_updated_default_billing_information_fiscal_representative.additional_properties = d
        return a02_response_200_updated_default_billing_information_fiscal_representative

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
