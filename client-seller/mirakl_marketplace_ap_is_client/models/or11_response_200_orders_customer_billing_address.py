from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersCustomerBillingAddress")


@_attrs_define
class OR11Response200OrdersCustomerBillingAddress:
    """
    Attributes:
        city (Union[Unset, str]): Address city
        civility (Union[Unset, str]): Civility of the person associated with the address
        company (Union[Unset, str]): Company of the person associated with the address
        company_2 (Union[Unset, str]): Second company information of the person associated with the address
        country (Union[Unset, str]): Address country
        country_iso_code (Union[Unset, str]): Country ISO 3166-1 code of the address
        firstname (Union[Unset, str]): First name of the person associated with the address
        lastname (Union[Unset, str]): Last name of the person associated with the address
        phone (Union[Unset, str]): Phone
        phone_secondary (Union[Unset, str]): Phone secondary
        state (Union[Unset, str]): Address state
        street_1 (Union[Unset, str]): First information line of the address street
        street_2 (Union[Unset, str]): Second information line of the address street
        zip_code (Union[Unset, str]): Address zip code
    """

    city: Union[Unset, str] = UNSET
    civility: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    company_2: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_iso_code: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    phone_secondary: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    street_1: Union[Unset, str] = UNSET
    street_2: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        civility = self.civility

        company = self.company

        company_2 = self.company_2

        country = self.country

        country_iso_code = self.country_iso_code

        firstname = self.firstname

        lastname = self.lastname

        phone = self.phone

        phone_secondary = self.phone_secondary

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
        if company is not UNSET:
            field_dict["company"] = company
        if company_2 is not UNSET:
            field_dict["company_2"] = company_2
        if country is not UNSET:
            field_dict["country"] = country
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

        company = d.pop("company", UNSET)

        company_2 = d.pop("company_2", UNSET)

        country = d.pop("country", UNSET)

        country_iso_code = d.pop("country_iso_code", UNSET)

        firstname = d.pop("firstname", UNSET)

        lastname = d.pop("lastname", UNSET)

        phone = d.pop("phone", UNSET)

        phone_secondary = d.pop("phone_secondary", UNSET)

        state = d.pop("state", UNSET)

        street_1 = d.pop("street_1", UNSET)

        street_2 = d.pop("street_2", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        or11_response_200_orders_customer_billing_address = cls(
            city=city,
            civility=civility,
            company=company,
            company_2=company_2,
            country=country,
            country_iso_code=country_iso_code,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            phone_secondary=phone_secondary,
            state=state,
            street_1=street_1,
            street_2=street_2,
            zip_code=zip_code,
        )

        or11_response_200_orders_customer_billing_address.additional_properties = d
        return or11_response_200_orders_customer_billing_address

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
