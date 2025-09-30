from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DR12Response200DataShippingToAddress")


@_attrs_define
class DR12Response200DataShippingToAddress:
    """
    Attributes:
        city (Union[Unset, str]): The city of the shipping address
        civility (Union[Unset, str]): The civility of the recipient (e.g., Mr., Mrs., Dr.)
        company (Union[Unset, str]): The company name of the shipping address
        company2 (Union[Unset, str]): The secondary company name of the shipping address
        country_iso_code (Union[Unset, str]): The ISO country code of the shipping address
        firstname (Union[Unset, str]): The first name of the recipient
        lastname (Union[Unset, str]): The last name of the recipient
        phone (Union[Unset, str]): The phone number of the recipient
        phone_secondary (Union[Unset, str]): The secondary phone number of the recipient
        state (Union[Unset, str]): The state of the shipping address
        street1 (Union[Unset, str]): The first line of the street address
        street2 (Union[Unset, str]): The second line of the street address
        zip_code (Union[Unset, str]): The zip code of the shipping address
    """

    city: Union[Unset, str] = UNSET
    civility: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    company2: Union[Unset, str] = UNSET
    country_iso_code: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    phone_secondary: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    street1: Union[Unset, str] = UNSET
    street2: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        civility = self.civility

        company = self.company

        company2 = self.company2

        country_iso_code = self.country_iso_code

        firstname = self.firstname

        lastname = self.lastname

        phone = self.phone

        phone_secondary = self.phone_secondary

        state = self.state

        street1 = self.street1

        street2 = self.street2

        zip_code = self.zip_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if civility is not UNSET:
            field_dict["civility"] = civility
        if company is not UNSET:
            field_dict["company"] = company
        if company2 is not UNSET:
            field_dict["company2"] = company2
        if country_iso_code is not UNSET:
            field_dict["country_iso_code"] = country_iso_code
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_secondary is not UNSET:
            field_dict["phone_secondary"] = phone_secondary
        if state is not UNSET:
            field_dict["state"] = state
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        civility = d.pop("civility", UNSET)

        company = d.pop("company", UNSET)

        company2 = d.pop("company2", UNSET)

        country_iso_code = d.pop("country_iso_code", UNSET)

        firstname = d.pop("firstname", UNSET)

        lastname = d.pop("lastname", UNSET)

        phone = d.pop("phone", UNSET)

        phone_secondary = d.pop("phone_secondary", UNSET)

        state = d.pop("state", UNSET)

        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        dr12_response_200_data_shipping_to_address = cls(
            city=city,
            civility=civility,
            company=company,
            company2=company2,
            country_iso_code=country_iso_code,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            phone_secondary=phone_secondary,
            state=state,
            street1=street1,
            street2=street2,
            zip_code=zip_code,
        )

        dr12_response_200_data_shipping_to_address.additional_properties = d
        return dr12_response_200_data_shipping_to_address

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
