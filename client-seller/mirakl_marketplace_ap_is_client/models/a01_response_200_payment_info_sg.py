from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A01Response200PaymentInfoSg")


@_attrs_define
class A01Response200PaymentInfoSg:
    """
    Attributes:
        bank_account_number (Union[Unset, str]): Bank Account Number
        bank_city (Union[Unset, str]): Bank city
        bank_key (Union[Unset, str]): Bank Key
        bank_name (Union[Unset, str]): Bank name
        bank_street (Union[Unset, str]): Bank street name
        bank_zip (Union[Unset, str]): Bank zip code
        owner (Union[Unset, str]): Name of the owner of the payment information
        swift_code (Union[Unset, str]): Bank account swift code
    """

    bank_account_number: Union[Unset, str] = UNSET
    bank_city: Union[Unset, str] = UNSET
    bank_key: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    bank_street: Union[Unset, str] = UNSET
    bank_zip: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    swift_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bank_account_number = self.bank_account_number

        bank_city = self.bank_city

        bank_key = self.bank_key

        bank_name = self.bank_name

        bank_street = self.bank_street

        bank_zip = self.bank_zip

        owner = self.owner

        swift_code = self.swift_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_account_number is not UNSET:
            field_dict["bank_account_number"] = bank_account_number
        if bank_city is not UNSET:
            field_dict["bank_city"] = bank_city
        if bank_key is not UNSET:
            field_dict["bank_key"] = bank_key
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if bank_street is not UNSET:
            field_dict["bank_street"] = bank_street
        if bank_zip is not UNSET:
            field_dict["bank_zip"] = bank_zip
        if owner is not UNSET:
            field_dict["owner"] = owner
        if swift_code is not UNSET:
            field_dict["swift_code"] = swift_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bank_account_number = d.pop("bank_account_number", UNSET)

        bank_city = d.pop("bank_city", UNSET)

        bank_key = d.pop("bank_key", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        bank_street = d.pop("bank_street", UNSET)

        bank_zip = d.pop("bank_zip", UNSET)

        owner = d.pop("owner", UNSET)

        swift_code = d.pop("swift_code", UNSET)

        a01_response_200_payment_info_sg = cls(
            bank_account_number=bank_account_number,
            bank_city=bank_city,
            bank_key=bank_key,
            bank_name=bank_name,
            bank_street=bank_street,
            bank_zip=bank_zip,
            owner=owner,
            swift_code=swift_code,
        )

        a01_response_200_payment_info_sg.additional_properties = d
        return a01_response_200_payment_info_sg

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
