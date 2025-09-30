from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IV01Response200InvoicesAutoInvoicePaymentInfo")


@_attrs_define
class IV01Response200InvoicesAutoInvoicePaymentInfo:
    """
    Attributes:
        type_ (Union[Unset, str]):
        bank_city (Union[Unset, str]): Bank city
        bank_name (Union[Unset, str]): Bank name
        bank_street (Union[Unset, str]): Bank street name
        bank_zip (Union[Unset, str]): Bank zip code
        owner (Union[Unset, str]): Name of the owner of the payment information
    """

    type_: Union[Unset, str] = UNSET
    bank_city: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    bank_street: Union[Unset, str] = UNSET
    bank_zip: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        bank_city = self.bank_city

        bank_name = self.bank_name

        bank_street = self.bank_street

        bank_zip = self.bank_zip

        owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["@type"] = type_
        if bank_city is not UNSET:
            field_dict["bank_city"] = bank_city
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if bank_street is not UNSET:
            field_dict["bank_street"] = bank_street
        if bank_zip is not UNSET:
            field_dict["bank_zip"] = bank_zip
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("@type", UNSET)

        bank_city = d.pop("bank_city", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        bank_street = d.pop("bank_street", UNSET)

        bank_zip = d.pop("bank_zip", UNSET)

        owner = d.pop("owner", UNSET)

        iv01_response_200_invoices_auto_invoice_payment_info = cls(
            type_=type_,
            bank_city=bank_city,
            bank_name=bank_name,
            bank_street=bank_street,
            bank_zip=bank_zip,
            owner=owner,
        )

        iv01_response_200_invoices_auto_invoice_payment_info.additional_properties = d
        return iv01_response_200_invoices_auto_invoice_payment_info

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
