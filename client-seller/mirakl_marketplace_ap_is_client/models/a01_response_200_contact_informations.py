from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A01Response200ContactInformations")


@_attrs_define
class A01Response200ContactInformations:
    """
    Attributes:
        city (Union[Unset, str]): City of the contact
        civility (Union[Unset, str]): Civility of the contact (Mr, Mrs, Miss or Neutral)
        country (Union[Unset, str]): Code ISO 3166-1 alpha-3 of the contact's country
        email (Union[Unset, str]): Email
        fax (Union[Unset, str]): Fax, max length: 20 characters.
        firstname (Union[Unset, str]): First name of the contact
        lastname (Union[Unset, str]): Last name of the contact
        phone (Union[Unset, str]): Phone
        phone_secondary (Union[Unset, str]): Secondary phone
        state (Union[Unset, str]): State (address) of the contact
        street1 (Union[Unset, str]): First line of the address of the contact
        street2 (Union[Unset, str]): Second line of the address of the contact
        web_site (Union[Unset, str]): Website of the shop
        zip_code (Union[Unset, str]): Zip code of the contact
    """

    city: Union[Unset, str] = UNSET
    civility: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    phone_secondary: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    street1: Union[Unset, str] = UNSET
    street2: Union[Unset, str] = UNSET
    web_site: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        civility = self.civility

        country = self.country

        email = self.email

        fax = self.fax

        firstname = self.firstname

        lastname = self.lastname

        phone = self.phone

        phone_secondary = self.phone_secondary

        state = self.state

        street1 = self.street1

        street2 = self.street2

        web_site = self.web_site

        zip_code = self.zip_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if civility is not UNSET:
            field_dict["civility"] = civility
        if country is not UNSET:
            field_dict["country"] = country
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
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
        if web_site is not UNSET:
            field_dict["web_site"] = web_site
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        civility = d.pop("civility", UNSET)

        country = d.pop("country", UNSET)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        firstname = d.pop("firstname", UNSET)

        lastname = d.pop("lastname", UNSET)

        phone = d.pop("phone", UNSET)

        phone_secondary = d.pop("phone_secondary", UNSET)

        state = d.pop("state", UNSET)

        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        web_site = d.pop("web_site", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        a01_response_200_contact_informations = cls(
            city=city,
            civility=civility,
            country=country,
            email=email,
            fax=fax,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            phone_secondary=phone_secondary,
            state=state,
            street1=street1,
            street2=street2,
            web_site=web_site,
            zip_code=zip_code,
        )

        a01_response_200_contact_informations.additional_properties = d
        return a01_response_200_contact_informations

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
