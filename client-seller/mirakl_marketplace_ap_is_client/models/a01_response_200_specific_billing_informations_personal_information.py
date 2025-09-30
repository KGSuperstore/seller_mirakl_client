import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="A01Response200SpecificBillingInformationsPersonalInformation")


@_attrs_define
class A01Response200SpecificBillingInformationsPersonalInformation:
    """
    Attributes:
        birth_city (Union[Unset, str]): The city of birth of the shop owner.
            <br/><i>Applies only when the shop is <code>non professional</code> or <code>professional sole
            trader</code>.</i>
        birth_country (Union[Unset, str]): The country of birth of the shop owner.
            <br/><i>Applies only when the shop is <code>non professional</code> or <code>professional sole
            trader</code>.</i>
        birth_date (Union[Unset, datetime.date]): The birth date of the shop owner.
            <br/><i>Applies only when the shop is <code>non professional</code> or <code>professional sole
            trader</code>.</i>
        civility (Union[Unset, str]): The civility of the shop owner.
            <br/><i>Applies only when the shop is <code>non professional</code> or <code>professional sole
            trader</code>.</i>
        first_name (Union[Unset, str]): The first name of the shop owner.
            <br/><i>Applies only when the shop is <code>non professional</code> or <code>professional sole
            trader</code>.</i>
        last_name (Union[Unset, str]): The last name of the shop owner.
            <br/><i>Applies only when the shop is <code>non professional</code> or <code>professional sole
            trader</code>.</i>
    """

    birth_city: Union[Unset, str] = UNSET
    birth_country: Union[Unset, str] = UNSET
    birth_date: Union[Unset, datetime.date] = UNSET
    civility: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        birth_city = self.birth_city

        birth_country = self.birth_country

        birth_date: Union[Unset, str] = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.isoformat()

        civility = self.civility

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if birth_city is not UNSET:
            field_dict["birth_city"] = birth_city
        if birth_country is not UNSET:
            field_dict["birth_country"] = birth_country
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date
        if civility is not UNSET:
            field_dict["civility"] = civility
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        birth_city = d.pop("birth_city", UNSET)

        birth_country = d.pop("birth_country", UNSET)

        _birth_date = d.pop("birth_date", UNSET)
        birth_date: Union[Unset, datetime.date]
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = isoparse(_birth_date).date()

        civility = d.pop("civility", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        a01_response_200_specific_billing_informations_personal_information = cls(
            birth_city=birth_city,
            birth_country=birth_country,
            birth_date=birth_date,
            civility=civility,
            first_name=first_name,
            last_name=last_name,
        )

        a01_response_200_specific_billing_informations_personal_information.additional_properties = d
        return a01_response_200_specific_billing_informations_personal_information

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
