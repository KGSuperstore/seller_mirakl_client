from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A01Response200BillingInfo")


@_attrs_define
class A01Response200BillingInfo:
    """
    Attributes:
        bank_city (Union[Unset, str]): City of the bank
        bank_name (Union[Unset, str]): Name of the bank
        bank_street (Union[Unset, str]): Address of the bank
        bic (Union[Unset, str]): BIC of the bank associated to the account
        iban (Union[Unset, str]): IBAN of the bank account
        owner (Union[Unset, str]): Name of the owner of the bank account
        zip_code (Union[Unset, str]): Zip code of the bank
    """

    bank_city: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    bank_street: Union[Unset, str] = UNSET
    bic: Union[Unset, str] = UNSET
    iban: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bank_city = self.bank_city

        bank_name = self.bank_name

        bank_street = self.bank_street

        bic = self.bic

        iban = self.iban

        owner = self.owner

        zip_code = self.zip_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_city is not UNSET:
            field_dict["bank_city"] = bank_city
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if bank_street is not UNSET:
            field_dict["bank_street"] = bank_street
        if bic is not UNSET:
            field_dict["bic"] = bic
        if iban is not UNSET:
            field_dict["iban"] = iban
        if owner is not UNSET:
            field_dict["owner"] = owner
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bank_city = d.pop("bank_city", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        bank_street = d.pop("bank_street", UNSET)

        bic = d.pop("bic", UNSET)

        iban = d.pop("iban", UNSET)

        owner = d.pop("owner", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        a01_response_200_billing_info = cls(
            bank_city=bank_city,
            bank_name=bank_name,
            bank_street=bank_street,
            bic=bic,
            iban=iban,
            owner=owner,
            zip_code=zip_code,
        )

        a01_response_200_billing_info.additional_properties = d
        return a01_response_200_billing_info

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
